from flask import Flask
from flask_mysqldb import MySQL
from views import *

app = Flask(__name__)
app.config.from_pyfile('config.py')

db = MySQL(app)

if __name__ == 'main':
app.run(debug=True)
