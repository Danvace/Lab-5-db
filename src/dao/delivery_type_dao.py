from src.dao.general_dao import GeneralDao
from src.model.delivery_type import DeliveryType


class DeliveryTypeDao(GeneralDao):
    _domain_type = DeliveryType
