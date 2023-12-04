from src.dao.category_dao import CategoryDao
from src.dao.characteristic_dao import CharacteristicDAO
from src.dao.delivery_dao import DeliveryDao
from src.dao.delivery_type_dao import DeliveryTypeDao
from src.dao.order_dao import OrderDao
from src.dao.product_dao import ProductDao
from src.dao.review_dao import ReviewDao
from src.dao.user_dao import UserDao

category_dao = CategoryDao()
characteristic_dao = CharacteristicDAO()
delivery_dao = DeliveryDao()
delivery_type_dao = DeliveryTypeDao()
order_dao = OrderDao()
product_dao = ProductDao()
review_dao = ReviewDao()
user_dao = UserDao()
