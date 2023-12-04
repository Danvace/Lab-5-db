from flask import Blueprint, make_response, request

from src.model.review import Review
from src.service import review_service

review_bp = Blueprint('review', __name__, url_prefix='/review')


@review_bp.get('')
def get_all_reviews():
    reviews = review_service.find_all()
    reviews_dto = list(map(lambda x: x.put_into_dto(), reviews))
    return make_response(reviews_dto, 200)


@review_bp.get('/<int:review_id>')
def get_review(review_id: int):
    review = review_service.find_by_id(review_id)
    if review is None:
        return make_response("Review not found", 404)
    return make_response(review.put_into_dto(), 200)


@review_bp.post('')
def create_review():
    content = request.get_json()
    review = Review.create_from_dto(content)
    review = review_service.create(review)
    return make_response(review.put_into_dto(), 201)


@review_bp.put('/<int:review_id>')
def update_review(review_id: int):
    content = request.get_json()
    review = Review.create_from_dto(content)
    review_service.update(review_id, review)
    return make_response("Review updated", 200)


@review_bp.delete('/<int:review_id>')
def delete_review(review_id: int):
    review = review_service.find_by_id(review_id)
    if review is None:
        return make_response("Review not found", 404)
    review_service.delete(review_id)
    return make_response("Review deleted", 200)
