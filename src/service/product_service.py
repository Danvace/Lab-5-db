from src.dao import product_dao
from src.service.general_service import GeneralService


class ProductService(GeneralService):
    _dao = product_dao
