import httplib

import pandas as pd
from flask import Flask, render_template, request, make_response

from database.database import engine, get_sql_query, get_sql_delete_query, select_query_for
from model.csvdata import parse_csv_to_model, check_column_with_model

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/data')
def data_table():
    data_frame = pd.read_sql_table('url', engine)
    csv_array = parse_csv_to_model(data_frame)
    return render_template('table.html', csvArray=csv_array)


@app.route('/filter')
def filter_data_table():
    sql_query = get_sql_query()
    data_frame = pd.read_sql_query(sql_query, engine)
    csv_array = parse_csv_to_model(data_frame)
    return render_template('table.html', csvArray=csv_array)


@app.route('/upload_file', methods=['POST'])
def upload_file():
    request_file = request.files['files']
    df = check_column_with_model(pd.read_csv(request_file, low_memory=False))
    csv_array = parse_csv_to_model(df)

    tmp_df = []
    to_drop_urls = []

    count = 0
    for idx, csv_obj in enumerate(csv_array):
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

    df.drop_duplicates('url', keep='first', inplace=True)

    for to_drop_url in to_drop_urls:
        df = df[df.url != to_drop_url]

    for tmp in tmp_df:
        df = df.append(tmp)
    df.to_sql('url', engine, if_exists='append', index=False)
    return '', httplib.NO_CONTENT


@app.route('/generate_csv')
def generate_csv():
    sql_query = get_sql_query()
    data_frame = pd.read_sql_query(sql_query, engine)
    csv_file = pd.DataFrame.to_csv(data_frame)
    response = make_response(csv_file)
    cd = 'attachment; filename=mycsv.csv'
    response.headers['Content-Disposition'] = cd
    response.mimetype = 'text/csv'
    return response


@app.route('/delete_db')
def delete_db():
    engine.execute(get_sql_delete_query())
    return '', httplib.NO_CONTENT


if __name__ == '__main__':
    app.run(debug=True)
