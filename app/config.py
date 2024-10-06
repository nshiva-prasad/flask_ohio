import os

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'dev_key')
    SQLALCHEMY_DATABASE_URI = 'sqlite:///wells.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
