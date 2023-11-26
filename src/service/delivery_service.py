from src.dao import delivery_dao
from src.service.general_service import GeneralService


class DeliveryService(GeneralService):
    _dao = delivery_dao
