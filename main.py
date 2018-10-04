import httplib

import pandas as pd
from flask import Flask, render_template, request, make_response

from database.database import engine, get_sql_query
from model.csvdata import parse_csv_to_model

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/data')
def data_table():
    # this needs to update in real time too and deliver some parameters
    dp = pd.read_sql_table('url', engine)
    csv_array = parse_csv_to_model(dp)
    return render_template('table.html', csvArray=csv_array)


@app.route('/filter')
def filter_data_table():
    sql_query = get_sql_query()
    dp = pd.read_sql_query(sql_query, engine)
    csv_array = parse_csv_to_model(dp)
    return render_template('table.html', csvArray=csv_array)


@app.route('/upload_file', methods=['POST'])
def upload_file():
    request_file = request.files['files']
    dp = pd.read_csv(request_file)
    csv_array = parse_csv_to_model(dp)

    for csv_obj in csv_array:
        dp['url'] = dp['url'].replace([csv_obj.url], csv_obj.split_url())

    dp.to_sql('url', engine, if_exists='append', index=False)
    return '', httplib.NO_CONTENT


# Todo return current table on index.html
@app.route('/generate_csv')
def generate_csv():
    sql_query = get_sql_query()
    dp = pd.read_sql_query(sql_query, engine)
    csv_file = pd.DataFrame.to_csv(dp)
    response = make_response(csv_file)
    cd = 'attachment; filename=mycsv.csv'
    response.headers['Content-Disposition'] = cd
    response.mimetype = 'text/csv'
    return response


if __name__ == '__main__':
    app.run(debug=True)
