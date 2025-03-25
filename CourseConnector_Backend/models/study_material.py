# models/study_material.py
from models import db

class StudyMaterial(db.Model):
    __tablename__ = 'study_material'

    id = db.Column(db.Integer, primary_key=True)
    course_id = db.Column(db.Integer, db.ForeignKey('course.id'), nullable=False)
    file_url = db.Column(db.String(500), nullable=False)
