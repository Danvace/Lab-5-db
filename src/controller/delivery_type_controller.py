from flask import Blueprint, make_response, request

from src.model.delivery_type import DeliveryType
from src.service import delivery_type_service

delivery_type_bp = Blueprint('delivery_type_controller', __name__, url_prefix='/delivery_type')


@delivery_type_bp.route('/<int:delivery_type_id>', methods=['GET'])
def get_delivery_type(delivery_type_id):
    delivery_type = delivery_type_service.find_by_id(delivery_type_id)
    if delivery_type is None:
        return make_response("Delivery type not found", 404)
    return make_response(delivery_type.put_into_dto(), 200)


@delivery_type_bp.route('', methods=['GET'])
def get_all_delivery_types():
    delivery_types = delivery_type_service.find_all()
    delivery_types_dto = list(map(lambda x: x.put_into_dto(), delivery_types))
    return make_response(delivery_types_dto, 200)


@delivery_type_bp.route('', methods=['POST'])
def create_delivery_type():
    delivery_type = request.get_json()
    delivery_type_obj = DeliveryType.create_from_dto(delivery_type)
    delivery_type_service.create(delivery_type_obj)
    return make_response(delivery_type, 201)


@delivery_type_bp.route('/<int:delivery_type_id>', methods=['PUT'])
def update_delivery_type(delivery_type_id):
    delivery_type = request.get_json()
    delivery_type_obj = DeliveryType.create_from_dto(delivery_type)
    delivery_type_service.update(delivery_type_id, delivery_type_obj)
    return make_response("Delivery type updated", 200)


@delivery_type_bp.route('/<int:delivery_type_id>', methods=['DELETE'])
def delete_delivery_type(delivery_type_id):
    if delivery_type_service.find_by_id(delivery_type_id) is None:
        return make_response("Delivery type not found", 404)
    delivery_type_service.delete(delivery_type_id)
    return make_response("Delivery type deleted", 200)
