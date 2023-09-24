from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

persistent_path = os.getenv("PERSISTENT_STORAGE_DIR", os.path.dirname(os.path.realpath(__file__)))

app = Flask(__name__)

db_path = os.path.join(persistent_path, "myproject.db")

app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql+pymysql://hyrule:hyrule@localhost/myproject'
app.config["SQL_ALCHEMY_ECHO"] = False
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy()

from app import views
from app import models

db.init_app(app)

with app.app_context():
    db.create_all()
