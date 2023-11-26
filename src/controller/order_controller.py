from flask import Blueprint, make_response, request, jsonify

from src.model.order import Order
from src.service import order_service, user_service, delivery_service

order_bp = Blueprint('order_controller', __name__, url_prefix='/order')


# @order_bp.route('/<int:order_id>', methods=['GET'])
# def get_order(order_id):
#     order = order_service.find_by_id(order_id)
#     if not order:
#         return make_response("Order not found", 404)
#     return make_response(order.put_into_dto(), 200)
# app.py (continued)

@order_bp.route('/<int:order_id>', methods=['GET'])
def get_order_with_details(order_id):
    order = order_service.find_by_id(order_id)

    if order is None:
        return jsonify({'error': 'Order not found'}), 404

    user = user_service.find_by_id(order.user_id)
    delivery = delivery_service.find_by_id(order.delivery_id)
    result = {
        'order': {
            'id': order.id,
            'date': order.date.isoformat(),
            'price': order.price,
            'user_id': order.user_id,
            'delivery_id': order.delivery_id,
        },
        'user': {
            'id': user.id,
            'user_name': user.user_name,
            'email': user.email,
            'create_time': user.create_time.isoformat(),
        },
        'delivery': {
            'id': delivery.id,
            'price': delivery.price,
            'delivery_type_type': delivery.delivery_type_type,
        }
    }

    return make_response(result, 200)


@order_bp.route('', methods=['GET'])
def get_all_orders_with_details():
    orders = order_service.find_all()
    orders_with_details = []

    for order in orders:
        user = user_service.find_by_id(order.user_id)
        delivery = delivery_service.find_by_id(order.delivery_id)
        order_details = {
            'order': {
                'id': order.id,
                'date': order.date.isoformat(),
                'price': order.price,
                'user_id': order.user_id,
                'delivery_id': order.delivery_id,
            },
            'user': {
                'id': user.id,
                'user_name': user.user_name,
                'email': user.email,
                'create_time': user.create_time.isoformat(),
            },
            'delivery': {
                'id': delivery.id,
                'price': delivery.price,
                'delivery_type_type': delivery.delivery_type_type,
            }
        }
        orders_with_details.append(order_details)

    return make_response(orders_with_details, 200)



@order_bp.route('', methods=['POST'])
def create_order():
    order = request.get_json()
    order_obj = Order.create_from_dto(order)
    order_service.create(order_obj)
    return make_response(order, 201)


@order_bp.route('/<int:order_id>', methods=['PUT'])
def update_order(order_id):
    order = request.get_json()
    order_obj = Order.create_from_dto(order)
    order_service.update(order_id, order_obj)
    return make_response("Order updated", 200)


@order_bp.route('/<int:order_id>', methods=['DELETE'])
def delete_order(order_id):
    if order_service.find_by_id(order_id) is None:
        return make_response("Order not found", 404)
    order_service.delete(order_id)
    return make_response("Order deleted", 200)
