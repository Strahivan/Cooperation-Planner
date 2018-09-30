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
def hello_world():
    # this needs to update in realtime too and deliver some parameters
    dp = pd.read_sql_table('url', engine)
    json_output = dp.to_json(orient='records')
    csvarray = [Csv(**k) for k in json.loads(json_output)]
    return render_template('index.html', csvArray=csvarray)


@app.route('/upload_file', methods=['POST'])
def upload_file():
    requestFile = request.files['files']
    dp = pd.read_csv(requestFile)
    # indexdata = 0

    json_output = dp.to_json(orient='records')
    csvarray = [Csv(**k) for k in json.loads(json_output)]

    for y in csvarray:
        if y.statuscode == 404:
            print y.statuscode
        else:
            parsedurl = urlparse(y.url).netloc
            dp['url'] = dp['url'].replace([y.url], parsedurl)
    dp.to_sql('url', engine, if_exists='append', index=False)
    return "nothing"


if __name__ == '__main__':
    app.run(debug=True)
