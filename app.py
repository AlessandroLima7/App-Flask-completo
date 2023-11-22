from flask import Flask
from flask_sqlalchemy import SQLAlchemy
  
app = Flask(__name__)
app.debug = True
  
# adding configuration for using a sqlite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
  
# Creating an SQLAlchemy instance
db = SQLAlchemy(app)

from views.home import home_bp

app.register_blueprint(blueprint=home_bp, url_prefix='/questions')
  
if __name__ == '__main__':
    app.run()