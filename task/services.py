import random

from flask import abort

from task import models, db, cache


@cache.memoize()
def get_product(product_id, review_paginator):
    """Get product from id and create paginator"""

    product = _get_product_from_id(product_id)

    reviews = models.Review.query.filter_by(asin=product.asin).paginate(page=review_paginator.page,
                                                                        per_page=review_paginator.per_page)

    return _get_product_with_review_pagination_json(product, reviews)


def create_review(product_id, review_args):
    """Create review from product id"""

    product = _get_product_from_id(product_id)

    # Create review
    review = models.Review(title=review_args.title, review=review_args.review, asin=product.asin)
    db.session.add(review)
    db.session.commit()

    # clear cache
    cache.delete_memoized(get_product)

    return {
               'message': 'success'
           }, 201


def _get_product_from_id(product_id):
    """Get product from id"""

    product = models.Product.query.get(product_id)
    if not product:
        abort(404, 'product not found')
    return product


def _get_product_with_review_pagination_json(product, reviews):
    """Return json data about product review with pagination"""

    return {
               'id': product.id,
               'title': product.title,
               'asin': product.asin,
               'reviews': _get_review(reviews),
               'pages': reviews.pages,
               'current_page': reviews.page,
               'next_num': _get_next_page(reviews, product.id),
               'prev_num': _get_perv_page(reviews, product.id),
               'limit': reviews.per_page,
               'number': random.randint(1, 10000)
           }, 200


def _get_review(reviews):
    """Return reviews"""

    return [{
        'id': r.id,
        'title': r.title,
        'review': r.review
    } for r in reviews.items]


def _get_next_page(reviews, product_id):
    """Return next page link"""

    if reviews.has_next:
        next_num = f'products/{product_id}/?page={reviews.next_num}&per_page={reviews.per_page}'
    else:
        next_num = 'null'
    return next_num


def _get_perv_page(reviews, product_id):
    """Return perv page link"""

    if reviews.has_prev:
        prev_num = f'products/{product_id}/?page={reviews.prev_num}&per_page={reviews.per_page}'
    else:
        prev_num = reviews.prev_num
    return prev_num
