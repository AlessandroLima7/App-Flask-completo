from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
  
app = Flask(__name__)
  
# adding configuration for using a sqlite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
CORS(app, resources={r"/api": {"origins": "*"}})

# Creating an SQLAlchemy instance
db = SQLAlchemy(app)

from views.home import home_bp

app.register_blueprint(blueprint=home_bp, url_prefix='/questions')