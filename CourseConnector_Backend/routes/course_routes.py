# routes/course_routes.py
from flask import Blueprint, request
from functions.course_functions import add_course, remove_course, enroll_in_course, unenroll_from_course

bp = Blueprint("course", __name__, url_prefix="/course")

@bp.route('/add', methods=['POST'])
def add():
    data = request.json
    return add_course(data['name'], data['description'])

@bp.route('/remove/<int:course_id>', methods=['DELETE'])
def remove(course_id):
    return remove_course(course_id)

@bp.route('/enroll', methods=['POST'])
def enroll():
    data = request.json
    return enroll_in_course(data['user_id'], data['course_id'])

@bp.route('/unenroll', methods=['POST'])
def unenroll():
    data = request.json
    return unenroll_from_course(data['user_id'], data['course_id'])
