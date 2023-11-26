from flask import make_response
from typing_extensions import override

from src.dao import delivery_type_dao
from src.service.general_service import GeneralService


class DeliveryTypeService(GeneralService):
    _dao = delivery_type_dao

    @override
    def create(self, obj: object) -> object:
        _type = self._dao.find_by_id(obj.type)
        if _type:
            return make_response(f"Delivery type with type {obj.type} already exists", 400)
        return self._dao.create(obj)
