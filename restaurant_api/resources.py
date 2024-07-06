from flask_restful import Resource, Api, reqparse
from models import db, Restaurant

# Request parser to handle input data
parser = reqparse.RequestParser()
parser.add_argument('name')
parser.add_argument('location')
parser.add_argument('cuisine')
parser.add_argument('rating', type=float)
parser.add_argument('phone')
parser.add_argument('email')


class RestaurantList(Resource):
    def get(self):
        # Get a list of all restaurants
        restaurants = Restaurant.query.all()
        return [{'id': r.id, 'name': r.name, 'location': r.location, 'cuisine': r.cuisine, 'rating': r.rating, 'phone': r.phone, 'email': r.email} for r in restaurants]

    def post(self):
        # Add a new restaurant to the list
        args = parser.parse_args()
        restaurant = Restaurant(
            name=args['name'],
            location=args['location'],
            cuisine=args['cuisine'],
            rating=args['rating'],
            phone=args['phone'],
            email=args['email']
        )
        db.session.add(restaurant)
        db.session.commit()
        return {'id': restaurant.id}, 201


class RestaurantDetail(Resource):
    def get(self, restaurant_id):
        # Get details of a specific restaurant by ID
        restaurant = Restaurant.query.get_or_404(restaurant_id)
        return {
            'id': restaurant.id,
            'name': restaurant.name,
            'location': restaurant.location,
            'cuisine': restaurant.cuisine,
            'rating': restaurant.rating,
            'phone': restaurant.phone,
            'email': restaurant.email
        }

    def put(self, restaurant_id): 
        # Update details of a specific restaurant by ID
        args = parser.parse_args()
        restaurant = Restaurant.query.get_or_404(restaurant_id)
        restaurant.name = args['name']
        restaurant.location = args['location']
        restaurant.cuisine = args['cuisine']
        restaurant.rating = args['rating']
        restaurant.phone = args['phone']
        restaurant.email = args['email']
        db.session.commit()
        return {'message': 'Restaurant updated successfully'}

    def delete(self, restaurant_id):
        # Delete a specific restaurant by ID
        restaurant = Restaurant.query.get_or_404(restaurant_id)
        db.session.delete(restaurant)
        db.session.commit()
        return {'message': 'Restaurant deleted successfully'}

# Resource for filtering restaurants based on location or cuisine
class RestaurantFilter(Resource):
    def get(self):
        # Filter restaurants based on location or cuisine
        args = parser.parse_args()
        location = args.get('location')
        cuisine = args.get('cuisine')
        query = Restaurant.query
        if location:
            query = query.filter_by(location=location)
        if cuisine:
            query = query.filter_by(cuisine=cuisine)
        restaurants = query.all()
        return [{'id': r.id, 'name': r.name, 'location': r.location, 'cuisine': r.cuisine, 'rating': r.rating, 'phone': r.phone, 'email': r.email} for r in restaurants]
