from flask_sqlalchemy import SQLAlchemy
# from flask_migrate import Migrate

# Initialize SQLAlchemy
db = SQLAlchemy()
# migrate = Migrate(app, db)

# Define the Restaurant model
class Restaurant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    location = db.Column(db.String(120), nullable=False)
    cuisine = db.Column(db.String(80), nullable=False)
    rating = db.Column(db.Float, nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(80), nullable=False)
