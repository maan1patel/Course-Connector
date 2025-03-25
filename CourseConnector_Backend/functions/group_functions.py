# functions/group_functions.py
from models import db
from models.study_group import StudyGroup
from flask import jsonify

def create_study_group(course_id, name):
    group = StudyGroup(course_id=course_id, name=name)
    db.session.add(group)
    db.session.commit()
    return jsonify({"message": "Study group created successfully"}), 201

def join_study_group(group_id, user_id):
    # Add logic for users joining a group
    return jsonify({"message": "Joined study group"}), 200
