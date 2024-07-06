import os

# Configuration class to set up database URI and other settings
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    # SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'restaurants.db')
    # SQLALCHEMY_DATABASE_URI = 'postgresql://username:password@localhost/restaurant_db'
    # SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://username:password@hostname/database' 
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root:12345Fff@localhost:3306/restrant_db'

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'your_secret_key'
