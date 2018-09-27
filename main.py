from flask import Flask, render_template
import database.queries as query
from model.csvdata import Csv
import json

app = Flask(__name__)

app.config.from_pyfile('database.cfg')

@app.route('/')
def hello_world():
    # this needs to update in realtime too and deliver some parameters
    dumps = json.dumps(query.get_url())
    csvarray = [Csv(**k) for k in json.loads(dumps)]
    return render_template('index.html', csvArray=csvarray)


@app.route('/input_File')
# this is a dynamic AJAX-request without a new request
def inputCsvFile():
    print "i worked"
    return "nothing"

# hier muss dann noch aus dem datahandler die entsprechenden Methoden aufgerufen werden, die die datenbank betreffen.

# Ausserdem muss in der View angepasst werden also der helloworld Methode dass Parameter als Liste in diesem Fall aus der DB mitgegeben und angezeigt werden

# Somit muss auch HTML angepasst werden (also die index.html)

# Ausserdem solltest du noch ein MYSQL-Skript schreiben, dass bei installation der App ausgefuehrt wird)

if __name__ == '__main__':
    app.run(debug=True)
