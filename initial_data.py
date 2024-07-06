from app import app
from models import db, Restaurant

# Populate initial data into the database
with app.app_context():
    db.create_all()
    sample_data = [
        { "id": 1, "name": "Pasta Paradise", "location": "Rome", "cuisine": "Italian", "rating": 4.5,
          "phone": "123-456-7890", "email": "info@pastaparadise.com"},
        { "id": 2, "name": "Curry King", "location": "Mumbai", "cuisine": "Indian", "rating": 4.7,
          "phone": "098-765-4321", "email": "contact@currykingdom.com"},
        { "id": 3, "name": "Sushi Suite", "location": "Tokyo", "cuisine": "Japanese", "rating": 4.9,
          "phone": "234-567-8901", "email": "reservations@sushisuite.com"},
        { "id": 4, "name": "Taco T", "location": "Mexico City", "cuisine": "Mexican", "rating": 4.4,
          "phone": "345-678-9012", "email": "info@tacoterritory.mx"}
    ]
    for data in sample_data:
        restaurant = Restaurant(**data)
        db.session.add(restaurant)
    db.session.commit()
