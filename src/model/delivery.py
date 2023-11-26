from typing import Dict

from src import db
from src.model.i_dto import IDto


class Delivery(db.Model, IDto):
    id = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.Float, nullable=False)
    delivery_type_type = db.Column(db.String(45), db.ForeignKey('DeliveryType.type'), nullable=False)

    # Specify the join condition explicitly
    delivery_type = db.relationship('DeliveryType', backref='deliveries', lazy=True,
                                    primaryjoin='Delivery.delivery_type_type == DeliveryType.type')

    def __init__(self, price, delivery_type_type):
        self.price = price
        self.delivery_type_type = delivery_type_type

    def put_into_dto(self) -> Dict[str, object]:
        return {
            "id": self.id,
            "price": self.price,
            "delivery_type_type": self.delivery_type_type,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, object]) -> object:
        delivery = Delivery(
            price=dto_dict['price'],
            delivery_type_type=dto_dict['delivery_type_type'],
        )
        return delivery
