from src.dao.general_dao import GeneralDao
from src.model.review import Review


class ReviewDao(GeneralDao):
    _domain_type = Review
