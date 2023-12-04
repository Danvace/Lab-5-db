from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_utils import database_exists, create_database

from config import Config
app = Flask(__name__)
db = SQLAlchemy()

app.config.from_object(Config)
db.init_app(app)

if not database_exists(app.config['SQLALCHEMY_DATABASE_URI']):
    create_database(app.config['SQLALCHEMY_DATABASE_URI'])
import src.model

with app.app_context():
    db.create_all()
from src.controller import register_routes

register_routes(app)