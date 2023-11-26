from src.dao import basket_dao
from src.service.general_service import GeneralService


class BasketService(GeneralService):
    _dao = basket_dao
