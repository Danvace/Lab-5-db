from src.dao.general_dao import GeneralDao
from src.model.category import Category


class CategoryDao(GeneralDao):
    _domain_type = Category
