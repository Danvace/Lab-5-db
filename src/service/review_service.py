from src.dao import review_dao
from src.service.general_service import GeneralService


class ReviewService(GeneralService):
    _dao = review_dao
