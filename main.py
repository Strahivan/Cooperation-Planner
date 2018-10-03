import httplib
import json

import pandas as pd
from flask import Flask, render_template, request, make_response
from sqlalchemy import create_engine

from model.csvdata import Csv
from util.query_builder import Builder

app = Flask(__name__)
engine = create_engine('mysql+mysqlconnector://root:iAmGod!4Sure@localhost:3306/urlinput')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/data')
def data_table():
    # this needs to update in real time too and deliver some parameters
    dp = pd.read_sql_table('url', engine)
    csv_array = __parse_csv_to_model(dp)
    return render_template('table.html', csvArray=csv_array)


@app.route('/filter')
def filter_data_table():
    sql_query = __get_sql_query()
    dp = pd.read_sql_query(sql_query, engine)
    csv_array = __parse_csv_to_model(dp)
    return render_template('table.html', csvArray=csv_array)


@app.route('/upload_file', methods=['POST'])
def upload_file():
    request_file = request.files['files']
    dp = pd.read_csv(request_file)
    csv_array = __parse_csv_to_model(dp)

    for csv_obj in csv_array:
        dp['url'] = dp['url'].replace([csv_obj.url], csv_obj.split_url())

    dp.to_sql('url', engine, if_exists='append', index=False)
    return '', httplib.NO_CONTENT


# Todo return current table on index.html
@app.route('/generate_csv')
def generate_csv():
    dp = pd.read_sql_query('SELECT url, statuscode, tld, status, inLink FROM url', engine)
    csv_file = pd.DataFrame.to_csv(dp)
    response = make_response(csv_file)
    cd = 'attachment; filename=mycsv.csv'
    response.headers['Content-Disposition'] = cd
    response.mimetype = 'text/csv'
    return response


def __parse_csv_to_model(dp):
    json_output = dp.to_json(orient='records')
    return [Csv(**k) for k in json.loads(json_output)]


def __get_sql_query():
    csv_filter = Csv(str(request.args['status']),
                     str(request.args['url']),
                     str(request.args['tld']),
                     str(request.args['inLink']),
                     str(request.args['statuscode']))

    builder = Builder('*')
    builder.from_table('url')

    count = 0
    for key, value in csv_filter.__dict__.iteritems():
        if value is not None and value is not '':
            if count == 0:
                builder.where(key, value)
            else:
                builder.and_where(key, value)
            count += 1

    return builder.build()


if __name__ == '__main__':
    app.run(debug=True)
