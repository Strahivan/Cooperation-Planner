import httplib
import json
from urlparse import urlparse

import pandas as pd
from flask import Flask, render_template, request
from sqlalchemy import create_engine

from model.csvdata import Csv

app = Flask(__name__)

app.config.from_pyfile('database.cfg')
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


@app.route('/upload_file', methods=['POST'])
def upload_file():
    request_file = request.files['files']
    dp = pd.read_csv(request_file)
    csv_array = __parse_csv_to_model(dp)

    for csv_obj in csv_array:
        # TODO: This method needs to be implemented in csvdata.py (checkStatusCode)
        if csv_obj.statuscode == 404:
            print csv_obj.statuscode
        else:
            # TODO: This method needs to be implemented in csvdata.py (splitURL)
            parsedurl = urlparse(csv_obj.url).netloc
            dp['url'] = dp['url'].replace([csv_obj.url], parsedurl)
    dp.to_sql('url', engine, if_exists='append', index=False)
    return '', httplib.NO_CONTENT


def __parse_csv_to_model(dp):
    json_output = dp.to_json(orient='records')
    return [Csv(**k) for k in json.loads(json_output)]


if __name__ == '__main__':
    app.run(debug=True)
