import os
from typing import Type


class BaseConfig:
    JSON_AS_ASCII = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = False
    DEBUG = False
    JSON_SORT_KEYS = True


class DevConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///offers.db'
    SQLALCHEMY_ECHO = True
    DEBUG = True


class ProdConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///offers.db'


def read_env() -> Type[BaseConfig]:
    match os.getenv('FLASK_ENV'):
        case 'development':
            return DevConfig
        case 'production':
            return ProdConfig
        case _:
            raise EnvironmentError('FLASK_ENV does not set')
