from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager

import config

app = Flask(__name__)

app.config.from_mapping(SQLALCHEMY_DATABASE_URI=config.POSTGRE_URI)
app.config.from_mapping(SQLALCHEMY_TRACK_MODIFICATIONS=False)
db = SQLAlchemy(app)

jwt = JWTManager(app)
