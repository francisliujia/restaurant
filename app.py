from flask import Flask, request
from flask_restful import Api
from models import db, Restaurant
from resources import RestaurantList, RestaurantDetail, RestaurantFilter
from config import Config

# from flask_sqlalchemy import SQLAlchemy
# from flask_migrate import Migrate

# create Flask app
app = Flask(__name__)
app.config.from_object(Config)
# db = SQLAlchemy(app)

# Initialize the database with the app
db.init_app(app)

# migrate = Migrate(app, db)

# Initialize Flask-RESTful API
api = Api(app)


# Create the database tables
with app.app_context():
    db.create_all()

# Add API resources
api.add_resource(RestaurantList, '/restaurants')
api.add_resource(RestaurantDetail, '/restaurants/<int:restaurant_id>')
api.add_resource(RestaurantFilter, '/restaurants/filter')

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)

