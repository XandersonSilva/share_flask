from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object('config')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///banco.db'  
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app.models import tables
from app.controllers import default