from flask import Flask, render_template
from flaskext.mysql import MySQL
app = Flask(__name__)

@app.route('/')
def hello_world():
# this needs to update in realtime too and deliver some parameters
    return render_template('index.html')

@app.route('/input_File')
# this is a dynamic AJAX-request without a new request
def inputCsvFile():
    print "i worked"
    return "nothing"


mysql = MySQL()
 
# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'iAmGod!4Sure'
app.config['MYSQL_DATABASE_DB'] = 'urlinput'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)

conn = mysql.connect()

# hier muss dann noch aus dem datahandler die entsprechenden Methoden aufgerufen werden, die die datenbank betreffen. 

# Ausserdem muss in der View angepasst werden also der helloworld Methode dass Parameter als Liste in diesem Fall aus der DB mitgegeben und angezeigt werden

# Somit muss auch HTML angepasst werden (also die index.html) 

# Ausserdem solltest du noch ein MYSQL-Skript schreiben, dass bei installation der App ausgefuehrt wird)

if __name__ == '__main__':
    app.run(debug=True)