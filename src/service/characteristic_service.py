from src.dao import characteristic_dao
from src.service.general_service import GeneralService


class CharacteristicService(GeneralService):
    _dao = characteristic_dao
