import os
from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

# create and config app
app = Flask(__name__)
app.config.from_object(os.getenv('CONFIG'))
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# register flask extensions
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from task import models, commands
