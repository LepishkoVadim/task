from flask_restful import Resource, reqparse

from task import api
from .services import get_product, create_review

# Parsing of arguments for pagination reviews
review_paginator_args = reqparse.RequestParser()
review_paginator_args.add_argument('page', type=int, help='current reviews page, need int', default=1)
review_paginator_args.add_argument('per_page', type=int, help='number of reviews per page, need int', default=5)

# Parsing of arguments for create review of product
review_put_args = reqparse.RequestParser()
review_put_args.add_argument('product_id', type=int, help='id product', required=True)
review_put_args.add_argument('title', type=str, help='title review, need str', required=True)
review_put_args.add_argument('review', type=str, help='review content, need str', required=True)


@api.resource('/api/v1/products/<int:product_id>/')
class ProductView(Resource):
    """View for product model"""

    def get(self, product_id):
        """Getting product from id"""

        review_paginator = review_paginator_args.parse_args()

        return get_product(product_id, review_paginator)


@api.resource('/api/v1/reviews/')
class ReviewView(Resource):
    """View for review model"""

    def put(self):
        """Creating review from product id"""

        args = review_put_args.parse_args()

        return create_review(args.product_id, args)
