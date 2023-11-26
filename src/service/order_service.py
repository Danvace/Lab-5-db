from src.dao import order_dao
from src.service.general_service import GeneralService


class OrderService(GeneralService):
    _dao = order_dao
