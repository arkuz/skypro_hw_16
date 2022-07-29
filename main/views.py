import logging
import const
import utils
from flask import Blueprint, render_template, request, jsonify

logger = logging.getLogger(__name__)
main_blueprint = Blueprint('main_blueprint', __name__, template_folder='templates')


@main_blueprint.route('/')
def index_page():
    return []




@main_blueprint.errorhandler(const.ERROR_404['code'])
def error_page_404(e):
    title = const.ERROR_404['code']
    text = const.ERROR_404['text']
    return render_template('error_page.html', title=title, text=text), const.ERROR_404['code']


@main_blueprint.errorhandler(const.ERROR_500['code'])
def error_page_500(e):
    title = const.ERROR_500['code']
    text = const.ERROR_500['text']
    return render_template('error_page.html', title=title, text=text), const.ERROR_500['text']


@main_blueprint.route('/api/posts/')
def api_posts():
    posts = utils.get_posts_all()
    logger.info('Обращение к "/api/posts/"')
    return jsonify(posts)


@main_blueprint.route('/api/post/<int:pk>/')
def api_post(pk):
    post = utils.get_post_by_pk(utils.get_posts_all(), pk)
    try:
        comments = utils.get_comments_by_post_id(utils.get_comments_all(), pk)
    except ValueError as e:
        logger.error(e)
        return jsonify({'type': 'error',
                        'code': const.ERROR_500['code'],
                        'message': str(e)})
    logger.info(f'Обращение к "/api/post/{pk}/"')
    return jsonify({'post': post,
                    'comments': comments})
