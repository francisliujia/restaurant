import os

# Configuration class to set up database URI and other settings
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    # SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'restaurants.db') # sqlite default db
    # SQLALCHEMY_DATABASE_URI = 'postgresql://username:password@localhost/restaurant_db' # postgreSQL db
    # SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://username:password@hostname/database' 
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root:12345Fff@localhost:3306/restrant_db'  # MySQl local db
    # SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://francisbbq:12345jfk@francisbbq.mysql.pythonanywhere-services.com/francisbbq$first_db1' # deployment db 

    
    # MYSQL_HOST = 'francisbbq.mysql.pythonanywhere-services.com'
    # MYSQL_USER = 'francisbbq'
    # MYSQL_PASSWORD = '12345jfk'
    # MYSQL_DB = 'francisbbq$default'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'your_secret_key'
