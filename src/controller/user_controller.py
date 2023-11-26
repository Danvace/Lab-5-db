from flask import Blueprint, make_response, request

from src.model.user import User
from src.service import user_service

user_bp = Blueprint('user_bp', __name__, url_prefix='/users')


@user_bp.route('/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = user_service.find_by_id(user_id)
    if user is None:
        return make_response("User not found", 404)
    return make_response(user.put_into_dto(), 200)


@user_bp.route('', methods=['GET'])
def get_all_users():
    users = user_service.find_all()
    users_dto = list(map(lambda x: x.put_into_dto(), users))
    return make_response(users_dto, 200)


@user_bp.route('', methods=['POST'])
def create_user():
    user = request.get_json()
    user_obj = User.create_from_dto(user)
    if user_service.find_by_email(user_obj.email) is not None:
        return make_response("User already exists", 400)
    user_service.create(user_obj)
    return make_response(user, 201)


@user_bp.route('/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    user = request.get_json()
    user_obj = User.create_from_dto(user)

    if user_service.find_by_id(user_id) is None:
        return make_response("User not found", 404)

    existing_user_by_email = user_service.find_by_email(user_obj.email)
    if existing_user_by_email is not None and existing_user_by_email.id != user_id:
        return make_response(f"User already exists with email {user_obj.email}", 400)

    user_service.update(user_id, user_obj)
    return make_response("User updated", 200)


@user_bp.route('/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    if user_service.find_by_id(user_id) is None:
        return make_response("User not found", 404)
    user_service.delete(user_id)
    return make_response("User deleted", 200)
