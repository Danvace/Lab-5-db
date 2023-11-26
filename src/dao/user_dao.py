from src.dao.general_dao import GeneralDao
from src.model.user import User


class UserDao(GeneralDao):
    _domain_type = User

    def get_user_by_email(self, email):
        return self._session.query(User).filter(User.email == email).first()
