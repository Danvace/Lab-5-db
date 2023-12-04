from typing import Dict

from src import db
from src.model.i_dto import IDto


class Review(db.Model, IDto):
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, nullable=False)
    response = db.Column(db.String(500))

    def __init__(self, product_id, response):
        self.product_id = product_id
        self.response = response

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, object]) -> object:
        return Review(
            product_id=dto_dict.get("product_id"),
            response=dto_dict.get("response")
        )

    def put_into_dto(self) -> Dict[str, object]:
        return {
            'id': self.id,
            'product_id': self.product_id,
            'response': self.response
        }
