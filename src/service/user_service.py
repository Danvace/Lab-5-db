from src.dao import user_dao
from src.service.general_service import GeneralService


class UserService(GeneralService):
    _dao = user_dao

    def find_by_email(self, email):
        return self._dao.get_user_by_email(email)
