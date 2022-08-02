import logging
import os.path
import const
from flask import Flask, jsonify
from blueprints.stock_market.models.stock_market import db
from blueprints.stock_market.views import stock_market_blueprint

logging.basicConfig(filename=os.path.join(const.BASE_DIR, 'log', 'log.log'),
                    level=logging.INFO,
                    format='%(asctime)s - [%(levelname)s] - %(name)s -'
                           ' (%(filename)s).%(funcName)s(%(lineno)d) - %(message)s')
logger = logging.getLogger(__name__)


def create_app() -> Flask:
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///offers.db'
    app.config['JSON_AS_ASCII'] = False
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
    app.register_blueprint(stock_market_blueprint)

    db.init_app(app)

    @app.errorhandler(const.ErrorCode.ERROR_404['code'])
    def error_page_404(e):
        return jsonify(const.ErrorCode.ERROR_404)

    @app.errorhandler(const.ErrorCode.ERROR_500['code'])
    def error_page_500(e):
        return jsonify(const.ErrorCode.ERROR_500)

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, port=5052)
