from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] ='postgresql://action@localhost/action'
app.config['SECRET_KEY'] = "alfred masterson"
db = SQLAlchemy(app)
from app import views
