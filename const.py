import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))


class ErrorCode:
    """Коды ошибок"""
    ERROR_404 = {'type': 'error', 'code': 404, 'message': 'Page not found'}
    ERROR_500 = {'type': 'error', 'code': 500, 'message': 'Internal Server Error'}


class ErrorMessage:
    """Пользовательские сообщения об ошибках"""
    EMPTY_RESULT = {'type': 'error', 'message': 'Empty result'}
    INVALID_JSON = {'type': 'error', 'message': 'Invalid JSON data'}
