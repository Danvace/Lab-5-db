from src.service.basket_has_product_service import BasketHasProductService
from src.service.basket_service import BasketService
from src.service.category_service import CategoryService
from src.service.characteristic_service import CharacteristicService
from src.service.delivery_service import DeliveryService
from src.service.delivery_type_service import DeliveryTypeService
from src.service.image_service import ImageService
from src.service.order_has_basket_service import OrderHasBasketService
from src.service.order_service import OrderService
from src.service.product_service import ProductService
from src.service.review_service import ReviewService
from src.service.user_service import UserService

basket_service = BasketService()
basket_has_product_service = BasketHasProductService()
category_service = CategoryService()
characteristic_service = CharacteristicService()
delivery_service = DeliveryService()
delivery_type_service = DeliveryTypeService()
image_service = ImageService()
order_service = OrderService()
order_has_basket_service = OrderHasBasketService()
product_service = ProductService()
review_service = ReviewService()
user_service = UserService()

