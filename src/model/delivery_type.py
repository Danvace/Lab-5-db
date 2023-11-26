from typing import Dict

from src import db
from src.model.i_dto import IDto


class DeliveryType(db.Model, IDto):
    __tablename__ = "DeliveryType"
    type = db.Column(db.String(45), primary_key=True)

    def __init__(self, type):
        self.type = type

    def put_into_dto(self) -> Dict[str, object]:
        return {
            "type": self.type
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, object]) -> object:
        return DeliveryType(
            type=dto_dict['type']
        )
