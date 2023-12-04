from src.service.category_service import CategoryService
from src.service.characteristic_service import CharacteristicService
from src.service.delivery_service import DeliveryService
from src.service.delivery_type_service import DeliveryTypeService
from src.service.order_service import OrderService
from src.service.product_service import ProductService
from src.service.review_service import ReviewService
from src.service.user_service import UserService

category_service = CategoryService()
characteristic_service = CharacteristicService()
delivery_service = DeliveryService()
delivery_type_service = DeliveryTypeService()
order_service = OrderService()
product_service = ProductService()
review_service = ReviewService()
user_service = UserService()

