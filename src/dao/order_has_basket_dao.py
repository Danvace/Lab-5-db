from src.dao.general_dao import GeneralDao
from src.model.order_has_basket import OrderHasBasket


class OrderHasBasketDao(GeneralDao):
    _domain_type = OrderHasBasket
