import os


class Config:
    """Base class for  project configuration"""
    DEBUG = os.getenv('FLASK_DEUBG')
    SECRET_KEY = os.getenv('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
