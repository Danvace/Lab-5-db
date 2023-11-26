from src.dao import category_dao
from src.service.general_service import GeneralService


class CategoryService(GeneralService):
    _dao = category_dao
