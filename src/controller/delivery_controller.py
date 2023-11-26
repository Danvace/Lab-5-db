from flask import Blueprint, make_response, jsonify, request

from src.model.delivery import Delivery
from src.service import delivery_service

delivery_bp = Blueprint('delivery_controller', __name__, url_prefix='/delivery')


@delivery_bp.route('', methods=["GET"])
def find_all_deliveries():
    deliveries = delivery_service.find_all()
    deliveries_dto = list(map(lambda x: x.put_into_dto(), deliveries))
    return make_response(jsonify(deliveries_dto), 200)


@delivery_bp.route('/<int:delivery_id>', methods=["GET"])
def find_by_id(delivery_id):
    delivery = delivery_service.find_by_id(delivery_id)
    if delivery is None:
        return make_response("delivery not found", 404)
    return make_response(jsonify(delivery.put_into_dto()), 200)


@delivery_bp.route('', methods=["POST"])
def create_delivery():
    delivery = request.get_json()
    delivery_obj = Delivery.create_from_dto(delivery)
    delivery_service.create(delivery_obj)
    return make_response(delivery, 201)


@delivery_bp.route('/<int:delivery_id>', methods=["PUT"])
def update_delivery(delivery_id):
    delivery = request.get_json()
    delivery_obj = Delivery.create_from_dto(delivery)
    if delivery_service.find_by_id(delivery_id) is None:
        return make_response("delivery not found", 404)
    delivery_service.update(delivery_id, delivery_obj)
    return make_response("delivery updated", 200)


@delivery_bp.route('/<int:delivery_id>', methods=["DELETE"])
def delete_delivery(delivery_id):
    if delivery_service.find_by_id(delivery_id) is None:
        return make_response("delivery not found", 404)
    delivery_service.delete(delivery_id)
    return make_response("delivery deleted", 200)