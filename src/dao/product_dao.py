from src.dao.general_dao import GeneralDao
from src.model.product import Product


class ProductDao(GeneralDao):
    _domain_type = Product
