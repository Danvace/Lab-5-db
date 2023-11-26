from src.dao.basket_dao import BasketDao
from src.dao.basket_has_product_dao import BasketHasProductDao
from src.dao.category_dao import CategoryDao
from src.dao.characteristic_dao import CharacteristicDAO
from src.dao.delivery_dao import DeliveryDao
from src.dao.delivery_type_dao import DeliveryTypeDao
from src.dao.image_dao import ImageDao
from src.dao.order_dao import OrderDao
from src.dao.order_has_basket_dao import OrderHasBasketDao
from src.dao.product_dao import ProductDao
from src.dao.review_dao import ReviewDao
from src.dao.user_dao import UserDao

basket_dao = BasketDao()
basket_has_product_dao = BasketHasProductDao()
category_dao = CategoryDao()
characteristic_dao = CharacteristicDAO()
delivery_dao = DeliveryDao()
delivery_type_dao = DeliveryTypeDao()
image_dao = ImageDao()
order_dao = OrderDao()
order_has_basket_dao = OrderHasBasketDao()
product_dao = ProductDao()
review_dao = ReviewDao()
user_dao = UserDao()
