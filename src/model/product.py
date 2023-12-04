from typing import Dict

from src import db
from src.model.i_dto import IDto


class Product(db.Model, IDto):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(45), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    price = db.Column(db.Float, nullable=False)
    category_name = db.Column(db.String(45), db.ForeignKey('category.name'), nullable=False)
    category = db.relationship('Category', backref='category')

    orders = db.relationship('Order', secondary='order_has_product', backref='products_in_order')

    def __init__(self, name, description, price, category_name):
        self.name = name
        self.description = description
        self.price = price
        self.category_name = category_name

    def put_into_dto(self) -> Dict[str, object]:
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "price": self.price,
            "category_name": self.category_name
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, object]) -> object:
        return Product(
            name=dto_dict.get("name"),
            description=dto_dict.get("description"),
            price=dto_dict.get("price"),
            category_name=dto_dict.get("category_name")
        )
