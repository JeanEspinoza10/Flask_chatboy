import os
from datetime import timedelta

class BaseConfig:
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = os.getenv('JWT_SECRET')


class DevelopmentConfig(BaseConfig):
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(hours=1)
    JWT_REFRESH_TOKEN_EXPIRES = timedelta(hours=3)
    MAIL_DEBUG = True


class ProductionConfig(BaseConfig):
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(minutes=30)
    JWT_REFRESH_TOKEN_EXPIRES = timedelta(hours=1)
    PROPAGATE_EXCEPTIONS = True


environment = {
    'development': DevelopmentConfig,
    'production': ProductionConfig
}
