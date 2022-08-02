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
    users = [user.to_dict() for user in db.session.query(User).all()]
    return jsonify(users)


@stock_market_blueprint.route('/users/<int:id>/')
def get_user_by_id(id):
    user = db.session.query(User).filter(User.id == id).first()
    if user:
        return jsonify(user.to_dict())
    return jsonify(const.ErrorMessage.EMPTY_RESULT)


@stock_market_blueprint.route('/users/<int:id>/', methods=['DELETE'])
def delete_user_by_id(id):
    user = User.query.get(id)
    if user:
        db.session.delete(user)
        db.session.commit()
        return jsonify(user.to_dict())
    return jsonify(const.ErrorMessage.EMPTY_RESULT)


@stock_market_blueprint.route('/orders/')
def get_orders():
    orders = [order.to_dict() for order in db.session.query(Order).all()]
    return jsonify(orders)


@stock_market_blueprint.route('/orders/<int:id>/')
def get_order_by_id(id):
    order = db.session.query(Order).filter(Order.id == id).first()
    if order:
        return jsonify(order.to_dict())
    return jsonify(const.ErrorMessage.EMPTY_RESULT)


@stock_market_blueprint.route('/orders/<int:id>/', methods=['DELETE'])
def delete_order_by_id(id):
    order = Order.query.get(id)
    if order:
        db.session.delete(order)
        db.session.commit()
        return jsonify(order.to_dict())
    return jsonify(const.ErrorMessage.EMPTY_RESULT)


@stock_market_blueprint.route('/offers/')
def get_offers():
    offers = [offer.to_dict() for offer in db.session.query(Offer).all()]
    return jsonify(offers)


@stock_market_blueprint.route('/offers/<int:id>/')
def get_offers_by_id(id):
    offer = db.session.query(Offer).filter(Offer.id == id).first()
    if offer:
        return jsonify(offer.to_dict())
    return jsonify(const.ErrorMessage.EMPTY_RESULT)


@stock_market_blueprint.route('/offers/<int:id>/', methods=['DELETE'])
def delete_offer_by_id(id):
    offer = Offer.query.get(id)
    if offer:
        db.session.delete(offer)
        db.session.commit()
        return jsonify(offer.to_dict())
    return jsonify(const.ErrorMessage.EMPTY_RESULT)
