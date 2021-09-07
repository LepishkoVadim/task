import os

from flask import Flask
from flask_migrate import Migrate
from flask_rest_paginate import Pagination
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api

# Create and config app
app = Flask(__name__)
app.config.from_object(os.getenv('CONFIG'))

# Register flask extensions
db = SQLAlchemy(app)
migrate = Migrate(app, db)
api = Api(app)
pagination = Pagination(app, db)

from task import models, commands, routes, services
