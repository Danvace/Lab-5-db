from src.dao.general_dao import GeneralDao
from src.model import Characteristic


class CharacteristicDAO(GeneralDao):
    _domain_type = Characteristic
