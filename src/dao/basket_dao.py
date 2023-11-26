from src.dao.general_dao import GeneralDao
from src.model.basket import Basket


class BasketDao(GeneralDao):
    _domain_type = Basket

