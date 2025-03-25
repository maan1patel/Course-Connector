# config.py
import os

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "supersecretkey")
    SQLALCHEMY_DATABASE_URI = "mysql://admin:admin1234@course-connector.c3sso8skw6vb.us-east-2.rds.amazonaws.com/course-connector"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    @staticmethod
    def init_app(app):
        pass
