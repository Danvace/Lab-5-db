from src import db


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(45), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    price = db.Column(db.Float, nullable=False)
    characteristic_id = db.Column(db.Integer, db.ForeignKey('characteristic.id'), nullable=False)
    category_name = db.Column(db.String(45), db.ForeignKey('category.name'), nullable=False)
    characteristic = db.relationship('Characteristic', backref='products')
    category = db.relationship('Category', backref='products')
