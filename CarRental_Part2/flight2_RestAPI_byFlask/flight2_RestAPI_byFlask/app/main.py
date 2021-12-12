# https://flask.palletsprojects.com/en/2.0.x/cli/
# export FLASK_APP=app.py / Windows: set FLASK_APP=app.py
# export FLASK_ENV=development/Windows: set FLASK_ENV=development
# flask run / Windows: python -m flask run
from flask import Flask, render_template, request
# import sqlite3  # sqlite3.connect()
import os, sys  
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
from function import config # import function from custom module
import pandas as pd

# create an instance of Flask object
app = Flask(__name__)

import requests
headers = {'Content-type':"application/json"}    
session = requests.Session()
session.headers.update(headers)

db_file = os.path.join("Rental.db")
db = config.sqlalchemy_sqlite3(db_file)

@app.route('/')
def home():
    heading = "Rental API"
    return render_template('index.html', section_title=heading)

@app.route('/list_model', methods=['GET','POST'])
def list_model():
    resultset = db.execute("SELECT * FROM specs") 
    rows = resultset.fetchall() #list of tuples
    df = pd.read_sql("SELECT * FROM specs", db) #dataframe
    return render_template(
        'index_api.html',
        heading="List of Cars",
        raw = f'raw:{rows}',
        dataframe = df.to_html())

@app.route('/list_cars_make', methods=['POST'])
def list_cars_make():
    data = {
        "vehiclemake": request.form['input_string']
    } # dictionary 
    df = pd.read_sql("SELECT * FROM specs WHERE vehiclemake like :vehiclemake", db, params=data)
    return render_template(
        'index_api.html',
        heading=f"Cars available {data['vehiclemake']}",
        dataframe = df.to_html())

if __name__ == "__main__":
    app.run(debug=True)