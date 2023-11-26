from src import db


class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    delivery_id = db.Column(db.Integer, db.ForeignKey('delivery.id'), nullable=False)
    user = db.relationship('User', backref='orders')
    delivery = db.relationship('Delivery', backref='orders')
