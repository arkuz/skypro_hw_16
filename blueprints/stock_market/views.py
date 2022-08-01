import logging
import const
from flask import (Blueprint,
                   jsonify)
from blueprints.stock_market.models.stock_market import (User,
                                                         Order,
                                                         Offer)
from blueprints.stock_market.models.stock_market import db

logger = logging.getLogger(__name__)
stock_market_blueprint = Blueprint('stock_market_blueprint', __name__)


@stock_market_blueprint.route('/users/')
def get_users():
    logger.info('Обращение к "/users/"')
    users = [user.to_dict() for user in db.session.query(User).all()]
    return jsonify(users)


@stock_market_blueprint.route('/users/<int:id>/')
def get_user_by_id(id):
    logger.info(f'Обращение к "/users/{id}/"')
    user = db.session.query(User).filter(User.id == id).first()
    if user:
        return jsonify(user.to_dict())
    return jsonify(const.ErrorMessage.EMPTY_RESULT)


@stock_market_blueprint.route('/orders/')
def get_orders():
    logger.info('Обращение к "/orders/"')
    orders = [order.to_dict() for order in db.session.query(Order).all()]
    return jsonify(orders)


@stock_market_blueprint.route('/orders/<int:id>/')
def get_order_by_id(id):
    logger.info(f'Обращение к "/orders/{id}/"')
    order = db.session.query(Order).filter(Order.id == id).first()
    if order:
        return jsonify(order.to_dict())
    return jsonify(const.ErrorMessage.EMPTY_RESULT)


@stock_market_blueprint.route('/offers/')
def get_offers():
    logger.info('Обращение к "/offers/"')
    offers = [offer.to_dict() for offer in db.session.query(Offer).all()]
    return jsonify(offers)


@stock_market_blueprint.route('/offers/<int:id>/')
def get_offers_by_id(id):
    logger.info(f'Обращение к "/offers/{id}/"')
    offer = db.session.query(Offer).filter(Offer.id == id).first()
    if offer:
        return jsonify(offer.to_dict())
    return jsonify(const.ErrorMessage.EMPTY_RESULT)


@stock_market_blueprint.errorhandler(const.ErrorCode.ERROR_404['code'])
def error_page_404(e):
    return jsonify(const.ErrorCode.ERROR_404)


@stock_market_blueprint.errorhandler(const.ErrorCode.ERROR_500['code'])
def error_page_500(e):
    return jsonify(const.ErrorCode.ERROR_500)
