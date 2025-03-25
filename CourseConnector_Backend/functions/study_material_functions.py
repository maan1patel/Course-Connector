# functions/study_material_functions.py
from models import db
from models.study_material import StudyMaterial
from flask import jsonify, request
import os

UPLOAD_FOLDER = "uploads"

def upload_study_material(course_id, file):
    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)

    file_path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(file_path)

    material = StudyMaterial(course_id=course_id, file_url=file_path)
    db.session.add(material)
    db.session.commit()
    return jsonify({"message": "File uploaded successfully", "file_url": file_path}), 201

def get_study_materials(course_id):
    materials = StudyMaterial.query.filter_by(course_id=course_id).all()
    return jsonify([{"id": m.id, "file_url": m.file_url} for m in materials])
