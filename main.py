import httplib
import os
import sys

import pandas as pd
from flask import Flask, render_template, request, make_response

from database.database import engine, get_sql_query, get_sql_delete_query, select_query_for
from model.csvdata import parse_csv_to_model, check_column_with_model

# ------- MAIN.PY -------

"""
This module is the main thread of the cooperation planning tool.

:copyright: (c)2018 by Michele Santoro, Steve Iva
:license: Apache 2.0, see LICENSE
"""

if getattr(sys, 'frozen', False):
    template_folder = os.path.join(sys._MEIPASS, 'templates')
    static_folder = os.path.join(sys._MEIPASS, 'static')
    app = Flask(__name__, template_folder=template_folder, static_folder=static_folder)
else:
    app = Flask(__name__)

"""
Loads the index.html-file in the first step.
The index.html makes an AJAX request to '/data' and thus loads the table.html.
"""


@app.route('/')
def index():
    return render_template('index.html')


"""
Loads the data table from the database. Then it takes the data_frame and parses it into a csv_array and returns it
to the table.html. Loads the table.html in the last step.

data_frame = creates a panda data_frame with the data from the database.
"""


@app.route('/data')
def data_table():
    data_frame = pd.read_sql_table('url', engine)
    csv_array = parse_csv_to_model(data_frame)
    return render_template('table.html', csvArray=csv_array)


"""
sql_query = gets the filter parameters from the request (user input)
data_frame = runs through the database with the filter parameters and loads them
It then takes the data_frame and parses it into a csv_array and returns this
to the table.html. Loads the table.html in the last step.
"""


@app.route('/filter')
def filter_data_table():
    sql_query = get_sql_query()
    data_frame = pd.read_sql_query(sql_query, engine)
    csv_array = parse_csv_to_model(data_frame)
    return render_template('table.html', csvArray=csv_array)


"""
The  CSV file is drawn as an HTML element and checks the entries with regard to their structure with
the check_column_with_model-Method. All entries that do not fit structurally will be deleted, otherwise
the application stores the "correct" elements in the object data_frame.

Then the data_frame is parsed to a CSV array again.

The first for-loop with idx and csv_object checks if it is a 404 error (sql_query is None if 404 error),
and whether the entry already exists in the database.
If it jumps out of the IF-Statement, it goes into the else and cuts the URL and TLD out.

At data_frame.to_sql the application then writes all input into the database.

"""


@app.route('/upload_file', methods=['POST'])
def upload_file():
    request_file = request.files['files']
    df = check_column_with_model(pd.read_csv(request_file, low_memory=False))
    csv_array = parse_csv_to_model(df)

    tmp_df = []
    to_drop_urls = []

    count = 0
    for idx, csv_obj in enumerate(csv_array):
        if csv_obj.split_tld() is not None:
            df.set_value(idx, 'url', csv_obj.split_url())
            df.set_value(idx, 'tld', csv_obj.split_tld())
            if csv_obj.statuscode == 404:
                tmp_df.append(df.iloc[idx - count].copy())
                df.drop(idx, inplace=True)
                count += 1
            sql_query = select_query_for(csv_obj.url, csv_obj.statuscode)
            if sql_query is not None and not pd.read_sql_query(sql_query, engine).empty:
                pd.read_sql_query(sql_query, engine)
                to_drop_urls.append(csv_obj.split_url())
        else:
            df.drop(idx, inplace=True)
            count += 1

    df.drop_duplicates('url', keep='first', inplace=True)

    for to_drop_url in to_drop_urls:
        df = df[df.url != to_drop_url]

    for tmp in tmp_df:
        df = df.append(tmp)
    df.to_sql('url', engine, if_exists='append', index=False)
    return '', httplib.NO_CONTENT


"""
sql_query = get_sql_query pulls out the filter parameters from the user input and creates a data_frame and then a CSV file.
Writes this to a CSV file and returns it as a response (for download).
"""


@app.route('/generate_csv')
def generate_csv():
    sql_query = get_sql_query()
    df = pd.read_sql_query(sql_query, engine)
    df.drop('id', axis=1, inplace=True)
    csv_file = pd.DataFrame.to_csv(df, encoding='UTF-8', index=False)
    response = make_response(csv_file)
    cd = 'attachment; filename=mycsv.csv'
    response.headers['Content-Disposition'] = cd
    response.mimetype = 'text/csv'
    return response


"""
Deletes the database.
"""


@app.route('/delete_db')
def delete_db():
    engine.execute(get_sql_delete_query())
    return '', httplib.NO_CONTENT


if __name__ == '__main__':
    app.run()
