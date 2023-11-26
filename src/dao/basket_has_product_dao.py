from src.dao.general_dao import GeneralDao
from src.model.basket_has_product import BasketHasProduct


class BasketHasProductDao(GeneralDao):
    _domain_type = BasketHasProduct
