# functions/course_functions.py
from models import db
from models.course import Course
from models.enrollment import Enrollment
from flask import jsonify

def add_course(name, description):
    course = Course(name=name, description=description)
    db.session.add(course)
    db.session.commit()
    return jsonify({"message": "Course added successfully"}), 201

def remove_course(course_id):
    course = Course.query.get(course_id)
    if not course:
        return jsonify({"error": "Course not found"}), 404

    db.session.delete(course)
    db.session.commit()
    return jsonify({"message": "Course removed successfully"}), 200

def enroll_in_course(user_id, course_id):
    enrollment = Enrollment(user_id=user_id, course_id=course_id)
    db.session.add(enrollment)
    db.session.commit()
    return jsonify({"message": "Enrolled successfully"}), 201

def unenroll_from_course(user_id, course_id):
    enrollment = Enrollment.query.filter_by(user_id=user_id, course_id=course_id).first()
    if not enrollment:
        return jsonify({"error": "Enrollment not found"}), 404

    db.session.delete(enrollment)
    db.session.commit()
    return jsonify({"message": "Unenrolled successfully"}), 200
