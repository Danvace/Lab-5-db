from src import db


class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    response = db.Column(db.String(500))
    product = db.relationship('Product', backref='reviews')
