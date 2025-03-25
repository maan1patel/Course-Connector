# routes/discussion_routes.py
from flask import Blueprint, request
from functions.discussion_functions import post_message, get_messages

bp = Blueprint("discussion", __name__, url_prefix="/discussion")

@bp.route('/post', methods=['POST'])
def post():
    data = request.json
    return post_message(data['group_id'], data['user_id'], data['message'])

@bp.route('/get/<int:group_id>', methods=['GET'])
def get_messages_route(group_id):
    return get_messages(group_id)
