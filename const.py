import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

DATA_PATH = os.path.join(BASE_DIR, 'data')
OFFERS_PATH = os.path.join(DATA_PATH, 'offers.json')
ORDERS_PATH = os.path.join(DATA_PATH, 'orders.json')
USERS_PATH = os.path.join(DATA_PATH, 'users.json')

ERROR_404 = {'code': 404, 'text': 'Page not found'}
ERROR_500 = {'code': 500, 'text': 'Internal Server Error'}
