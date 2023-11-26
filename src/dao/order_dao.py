from src.dao.general_dao import GeneralDao
from src.model.order import Order


class OrderDao(GeneralDao):
    _domain_type = Order
