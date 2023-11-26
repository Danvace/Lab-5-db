from src import db


class Basket(db.Model):
    id = db.Column(db.Integer, primary_key=True)
