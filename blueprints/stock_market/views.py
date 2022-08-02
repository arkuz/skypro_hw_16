import logging
from datetime import datetime

import const
from flask import (Blueprint,
                   jsonify,
                   request)
from blueprints.stock_market.models.stock_market import (User,
                                                         Order,
                                                         Offer)
from blueprints.stock_market.models.stock_market import db
from sqlalchemy import desc

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


@stock_market_blueprint.route('/users/', methods=['POST'])
def add_user():
    user_data = request.get_json(force=True, silent=True)
    if user_data:
        if user_data.get('id'):
            del user_data['id']
        user = User(**user_data)
        db.session.add(user)
        db.session.commit()
        added_user = db.session.query(User).order_by(desc(User.id)).first()
        return jsonify(added_user.to_dict())
    return jsonify(const.ErrorMessage.INVALID_JSON)


@stock_market_blueprint.route('/users/<int:id>/', methods=['PUT'])
def edit_user_by_id(id):
    user = db.session.query(User).filter(User.id == id).first()
    if not user:
        return jsonify(const.ErrorMessage.EMPTY_RESULT)

    user_data = request.get_json(force=True, silent=True)
    if user_data:
        if user_data.get('id'):
            del user_data['id']

        for key, value in user_data.items():
            user.__setattr__(key, value)

        db.session.add(user)
        db.session.commit()
        edited_user = db.session.query(User).filter(User.id == id).first()
        return jsonify(edited_user.to_dict())
    return jsonify(const.ErrorMessage.INVALID_JSON)


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


@stock_market_blueprint.route('/orders/', methods=['POST'])
def add_order():
    order_data = request.get_json(force=True, silent=True)
    if order_data:
        if order_data.get('id'):
            del order_data['id']

        # конвертируем дату из строки в тип даты
        if order_data.get('start_date'):
            order_data['start_date'] = datetime.strptime(order_data['start_date'], '%m/%d/%Y').date()
        if order_data.get('end_date'):
            order_data['end_date'] = datetime.strptime(order_data['end_date'], '%m/%d/%Y').date()

        order = Order(**order_data)
        db.session.add(order)
        db.session.commit()
        added_order = db.session.query(Order).order_by(desc(Order.id)).first()
        return jsonify(added_order.to_dict())
    return jsonify(const.ErrorMessage.INVALID_JSON)


@stock_market_blueprint.route('/orders/<int:id>/', methods=['PUT'])
def edit_order_by_id(id):
    order = db.session.query(Order).filter(Order.id == id).first()
    if not order:
        return jsonify(const.ErrorMessage.EMPTY_RESULT)

    order_data = request.get_json(force=True, silent=True)
    if order_data:
        if order_data.get('id'):
            del order_data['id']

        # конвертируем дату из строки в тип даты
        if order_data.get('start_date'):
            order_data['start_date'] = datetime.strptime(order_data['start_date'], '%m/%d/%Y').date()
        if order_data.get('end_date'):
            order_data['end_date'] = datetime.strptime(order_data['end_date'], '%m/%d/%Y').date()

        for key, value in order_data.items():
            order.__setattr__(key, value)

        db.session.add(order)
        db.session.commit()
        edited_order = db.session.query(Order).filter(Order.id == id).first()
        return jsonify(edited_order.to_dict())
    return jsonify(const.ErrorMessage.INVALID_JSON)


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


@stock_market_blueprint.route('/offers/', methods=['POST'])
def add_offer():
    offer_data = request.get_json(force=True, silent=True)
    if offer_data:
        if offer_data.get('id'):
            del offer_data['id']
        offer = Offer(**offer_data)
        db.session.add(offer)
        db.session.commit()
        added_offer = db.session.query(Offer).order_by(desc(Offer.id)).first()
        return jsonify(added_offer.to_dict())
    return jsonify(const.ErrorMessage.INVALID_JSON)


@stock_market_blueprint.route('/offers/<int:id>/', methods=['PUT'])
def edit_offer_by_id(id):
    offer = db.session.query(Offer).filter(Offer.id == id).first()
    if not offer:
        return jsonify(const.ErrorMessage.EMPTY_RESULT)

    offer_data = request.get_json(force=True, silent=True)
    if offer_data:
        if offer_data.get('id'):
            del offer_data['id']

        for key, value in offer_data.items():
            offer.__setattr__(key, value)

        db.session.add(offer)
        db.session.commit()
        edited_offer = db.session.query(Offer).filter(Offer.id == id).first()
        return jsonify(edited_offer.to_dict())
    return jsonify(const.ErrorMessage.INVALID_JSON)


@stock_market_blueprint.route('/offers/<int:id>/', methods=['DELETE'])
def delete_offer_by_id(id):
    offer = Offer.query.get(id)
    if offer:
        db.session.delete(offer)
        db.session.commit()
        return jsonify(offer.to_dict())
    return jsonify(const.ErrorMessage.EMPTY_RESULT)
