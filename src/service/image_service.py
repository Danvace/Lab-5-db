from src.dao import image_dao
from src.service.general_service import GeneralService


class ImageService(GeneralService):
    _dao = image_dao
