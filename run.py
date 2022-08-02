import os

from app import create_app

from config import (DevConfig,
                    ProdConfig)

match os.getenv('FLASK_ENV'):
    case 'development':
        config = DevConfig
    case 'production':
        config = ProdConfig
    case _:
        raise EnvironmentError('FLASK_ENV does not set')

app = create_app(config=config)
