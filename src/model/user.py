from typing import Dict

from src import db
from src.model.i_dto import IDto


class User(db.Model, IDto):
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(255), unique=False, nullable=False)  # so I can have easy use in postman
    password = db.Column(db.String(100), nullable=False)
    create_time = db.Column(db.TIMESTAMP, nullable=False)

    def __init__(self, user_name, email, password, create_time):
        self.user_name = user_name
        self.email = email
        self.password = password
        self.create_time = create_time

    def put_into_dto(self) -> Dict[str, object]:
        return {
            "id": self.id,
            "user_name": self.user_name,
            "email": self.email,
            "password": self.password,
            "create_time": self.create_time
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, object]) -> object:
        user = User(
            user_name=dto_dict.get("user_name"),
            email=dto_dict.get("email"),
            password=dto_dict.get("password"),
            create_time=dto_dict.get("create_time")
        )
        return user
