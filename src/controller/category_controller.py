from flask import Blueprint, make_response, request

from src.model.category import Category
from src.service import category_service

category_bp = Blueprint('category_bp', __name__, url_prefix='/categories')


@category_bp.route('', methods=['GET'])
def get_all_categories():
    categories = category_service.find_all()
    categories_dto = list(map(lambda x: x.put_into_dto(), categories))
    return make_response(categories_dto, 200)


@category_bp.route('', methods=['POST'])
def create_category():
    content = request.get_json()
    category = Category.create_from_dto(content)
    category = category_service.create(category)
    return make_response(category.put_into_dto(), 201)


@category_bp.route('/<string:category_name>', methods=['DELETE'])
def delete_category(category_name: str):
    category = category_service.find_by_id(category_name)
    if category is None:
        return make_response("Category not found", 404)
    category_service.delete(category_name)
    return make_response("Category deleted", 200)
