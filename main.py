import json

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
    dp.to_sql('url', engine, if_exists='replace')
    return "nothing"


# hier muss dann noch aus dem datahandler die entsprechenden Methoden aufgerufen werden, die die datenbank betreffen.

# Ausserdem muss in der View angepasst werden also der helloworld Methode dass Parameter als Liste in diesem Fall aus der DB mitgegeben und angezeigt werden

# Somit muss auch HTML angepasst werden (also die index.html)

# Ausserdem solltest du noch ein MYSQL-Skript schreiben, dass bei installation der App ausgefuehrt wird)

if __name__ == '__main__':
    app.run(debug=True)
