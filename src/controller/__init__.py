from flask import Flask

from src.controller.category_controller import category_bp
from src.controller.characteristic_controller import characteristic_bp
from src.controller.delivery_controller import delivery_bp
from src.controller.delivery_type_controller import delivery_type_bp
from src.controller.order_controller import order_bp
from src.controller.procedure_controller import procedure_bp
from src.controller.product_controller import product_bp
from src.controller.reivew_controller import review_bp
from src.controller.user_controller import user_bp


def register_routes(app: Flask):
    app.register_blueprint(characteristic_bp)
    app.register_blueprint(user_bp)
    app.register_blueprint(delivery_type_bp)
    app.register_blueprint(delivery_bp)
    app.register_blueprint(order_bp)
    app.register_blueprint(category_bp)
    app.register_blueprint(product_bp)
    app.register_blueprint(review_bp)
    app.register_blueprint(procedure_bp)
