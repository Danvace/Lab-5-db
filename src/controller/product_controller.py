from flask import Blueprint, make_response, request

from src.model.product import Product
from src.service import product_service, category_service

product_bp = Blueprint('product_bp', __name__, url_prefix='/products')


@product_bp.route('', methods=['GET'])
def get_all_products():
    products = product_service.find_all()
    products_dto = list(map(lambda x: x.put_into_dto(), products))
    return make_response(products_dto, 200)


@product_bp.route('/<int:product_id>', methods=['GET'])
def get_product(product_id: int):
    product = product_service.find_by_id(product_id)
    if product is None:
        return make_response("Product not found", 404)
    return make_response(product.put_into_dto(), 200)


@product_bp.route('', methods=['POST'])
def create_product():
    content = request.get_json()
    product = Product.create_from_dto(content)
    product = product_service.create(product)
    return make_response(product.put_into_dto(), 201)


@product_bp.route('/<int:product_id>', methods=['PUT'])
def update_product(product_id: int):
    content = request.get_json()
    product = Product.create_from_dto(content)
    category = category_service.find_by_id(content.get("category_name"))
    if category is None:
        return make_response("Category not found", 404)
    product_service.update(product_id, product)
    return make_response("Product updated", 200)


@product_bp.route('/<int:product_id>', methods=['DELETE'])
def delete_product(product_id: int):
    product = product_service.find_by_id(product_id)
    if product is None:
        return make_response("Product not found", 404)
    product_service.delete(product_id)
    return make_response("Product deleted", 200)
