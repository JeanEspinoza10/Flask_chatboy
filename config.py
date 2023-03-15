import os
from datetime import timedelta

class BaseConfig:
    pass


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
