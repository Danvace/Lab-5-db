from src.dao.general_dao import GeneralDao
from src.model.delivery import Delivery


class DeliveryDao(GeneralDao):
    _domain_type = Delivery
    