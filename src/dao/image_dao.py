from src.dao.general_dao import GeneralDao
from src.model.image import Image


class ImageDao(GeneralDao):
    _domain_type = Image
