from src import db


class Category(db.Model):
    name = db.Column(db.String(45), primary_key=True)
