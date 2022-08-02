import os
from app import db, create_app
from const import BASE_DIR
from utils import _load_json_file
from datetime import datetime
from blueprints.stock_market.models.stock_market import (User,
                                                         Order,
                                                         Offer)

from config import read_env

FIXTURES_DIR = os.path.join(BASE_DIR, 'blueprints', 'stock_market', 'db', 'fixtures')
OFFERS_DIR = os.path.join(FIXTURES_DIR, 'offers.json')
ORDERS_DIR = os.path.join(FIXTURES_DIR, 'orders.json')
USERS_DIR = os.path.join(FIXTURES_DIR, 'users.json')


def load_users() -> list[dict]:
    return _load_json_file(USERS_DIR)


def load_orders() -> list[dict]:
    return _load_json_file(ORDERS_DIR)


def load_offers() -> list[dict]:
    return _load_json_file(OFFERS_DIR)


def add_users() -> None:
    users = load_users()
    prepared_users = [User(**user) for user in users]
    db.session.add_all(prepared_users)
    db.session.commit()


def add_orders() -> None:
    orders = load_orders()
    prepared_orders = []
    for order in orders:
        prepared_orders.append(Order(id=order['id'],
                                     name=order['name'],
                                     description=order['description'],
                                     start_date=datetime.strptime(order['start_date'], '%m/%d/%Y').date(),
                                     end_date=datetime.strptime(order['end_date'], '%m/%d/%Y').date(),
                                     address=order['address'],
                                     price=order['price'],
                                     customer_id=order['customer_id'],
                                     executor_id=order['executor_id']))
        db.session.add_all(prepared_orders)
        db.session.commit()


def add_offers() -> None:
    offers = load_offers()
    prepared_offers = [Offer(**offer) for offer in offers]
    db.session.add_all(prepared_offers)
    db.session.commit()


def init_db() -> None:
    config = read_env()
    app = create_app(config)
    with app.app_context():
        db.drop_all()
        db.create_all()
        add_users()
        add_orders()
        add_offers()


if __name__ == '__main__':
    init_db()
    print('Database initialized successfully')
