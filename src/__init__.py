from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config
app = Flask(__name__)
db = SQLAlchemy()

app.config.from_object(Config)
db.init_app(app)
with app.app_context():
    db.create_all()

from src.controller import register_routes
register_routes(app)
