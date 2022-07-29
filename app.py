import logging
from flask import Flask

from main.views import main_blueprint

logging.basicConfig(filename="log/log.log",
                    level=logging.INFO,
                    format='%(asctime)s - [%(levelname)s] - %(name)s -'
                           ' (%(filename)s).%(funcName)s(%(lineno)d) - %(message)s')
logger = logging.getLogger(__name__)

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////orders.db'

app.register_blueprint(main_blueprint)

if __name__ == '__main__':
    app.run()
