# routes/group_routes.py
from flask import Blueprint, request
from functions.group_functions import create_study_group, join_study_group

bp = Blueprint("group", __name__, url_prefix="/group")

@bp.route('/create', methods=['POST'])
def create():
    data = request.json
    return create_study_group(data['course_id'], data['name'])

@bp.route('/join', methods=['POST'])
def join():
    data = request.json
    return join_study_group(data['group_id'], data['user_id'])
