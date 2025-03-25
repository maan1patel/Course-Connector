# routes/material_routes.py
from flask import Blueprint, request
from functions.study_material_functions import upload_study_material, get_study_materials

bp = Blueprint("study_material", __name__, url_prefix="/study_material")

@bp.route('/upload', methods=['POST'])
def upload():
    course_id = request.form.get('course_id')
    file = request.files.get('file')
    return upload_study_material(course_id, file)

@bp.route('/get/<int:course_id>', methods=['GET'])
def get_materials(course_id):
    return get_study_materials(course_id)
