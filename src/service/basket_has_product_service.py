from src.dao import basket_has_product_dao
from src.service.general_service import GeneralService


class BasketHasProductService(GeneralService):
    _dao = basket_has_product_dao
