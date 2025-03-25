# models/study_group.py
from models import db

class StudyGroup(db.Model):
    __tablename__ = 'study_group'

    id = db.Column(db.Integer, primary_key=True)
    course_id = db.Column(db.Integer, db.ForeignKey('course.id'), nullable=False)
    name = db.Column(db.String(255), nullable=False)
