from src.dao import order_has_basket_dao
from src.service.general_service import GeneralService


class OrderHasBasketService(GeneralService):
    _dao = order_has_basket_dao
