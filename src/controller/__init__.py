from flask import Flask

from src.controller.characteristic_controller import characteristic_bp
from src.controller.delivery_controller import delivery_bp
from src.controller.delivery_type_controller import delivery_type_bp
from src.controller.user_controller import user_bp


def register_routes(app: Flask):
    app.register_blueprint(characteristic_bp)
    app.register_blueprint(user_bp)
    app.register_blueprint(delivery_type_bp)
    app.register_blueprint(delivery_bp)