from flask import Blueprint, request, make_response, jsonify

from src.dao import characteristic_dao
from src.model import Characteristic
from src.service import characteristic_service

characteristic_bp = Blueprint('client_bp', __name__, url_prefix='/characteristic')


@characteristic_bp.route('/<int:characteristic_id>', methods=['GET'])
def get_client(characteristic_id):
    characteristic = characteristic_service.find_by_id(characteristic_id)
    if characteristic is None:
        return make_response("Characteristic not found", 404)
    return make_response(jsonify(characteristic.put_into_dto()), 200)


@characteristic_bp.route('', methods=['GET'])
def get_all_clients():
    characteristics = characteristic_dao.find_all()
    characteristics_dto = list(map(lambda x: x.put_into_dto(), characteristics))
    return make_response(jsonify(characteristics_dto), 200)


@characteristic_bp.route('', methods=['POST'])
def create_client():
    characteristic = request.get_json()
    characteristic_obj = Characteristic.create_from_dto(characteristic)
    characteristic_dao.create(characteristic_obj)
    return make_response(characteristic, 201)


@characteristic_bp.route('/<int:characteristic_id>', methods=['PUT'])
def update_client(characteristic_id):
    characteristic = request.get_json()
    characteristic_obj = Characteristic.create_from_dto(characteristic)
    characteristic_dao.update(characteristic_id, characteristic_obj)
    return make_response("Characteristic updated", 200)


@characteristic_bp.route('/<int:characteristic_id>', methods=['DELETE'])
def delete_client(characteristic_id):
    characteristic_dao.delete(characteristic_id)
    return make_response("Characteristic deleted", 200)
