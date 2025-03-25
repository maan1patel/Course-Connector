# routes/material_routes.py
from flask import Blueprint, request, jsonify
from functions.course_material_functions import upload_study_material, search_study_material

bp = Blueprint('materials', __name__, url_prefix='/materials')

@bp.route('/upload', methods=['POST'])
def upload():
    file = request.files.get('file')
    data = request.form.to_dict()
    result = upload_study_material(file, data)
    return jsonify(result)

@bp.route('/search', methods=['GET'])
def search():
    query = request.args.get('query')
    result = search_study_material(query)
    return jsonify(result)
