from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] ='c5b581ae872c7b70c4fc6b018ea74134'

ENV ='prod'

if ENV =='dev':
    app.debug = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:mechatronic@localhost/citizens'
else:
    app.debug =False
    app.config['SQLALCHEMY_DATABASE_URI'] ='postgresql://krcifxiizurbdm:a67028a1ef21b4eba093330e73e534ad6f0fff32288e0c7f58f6116f19ffb2da@ec2-54-166-37-125.compute-1.amazonaws.com:5432/d70638plmq6ng4'

db = SQLAlchemy(app)

from voting_app import route