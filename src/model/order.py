from typing import Dict

from src import db
from src.model.i_dto import IDto


class Order(db.Model, IDto):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, nullable=False)
    price = db.Column(db.Float, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    delivery_id = db.Column(db.Integer, db.ForeignKey('delivery.id'), nullable=False)

    user = db.relationship('User', backref='orders', foreign_keys=[user_id])
    delivery = db.relationship('Delivery', backref='orders')

    products = db.relationship('Product', secondary='order_has_product', backref='order')

    def __init__(self, date, user_id, delivery_id, price):
        self.date = date
        self.user_id = user_id
        self.delivery_id = delivery_id
        self.price = price

    def put_into_dto(self) -> Dict[str, object]:
        return {
            "id": self.id,
            "date": self.date,
            "user_id": self.user_id,
            "delivery_id": self.delivery_id,
            "price": self.price
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, object]) -> object:
        return Order(
            date=dto_dict.get("date"),
            user_id=dto_dict.get("user_id"),
            delivery_id=dto_dict.get("delivery_id"),
            price=dto_dict.get("price")
        )
