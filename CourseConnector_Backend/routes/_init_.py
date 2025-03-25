# routes/__init__.py
from flask import Flask
from routes import auth_routes, course_routes, material_routes, group_routes, discussion_routes

def register_routes(app: Flask):
    app.register_blueprint(auth_routes.bp)
    app.register_blueprint(course_routes.bp)
    app.register_blueprint(material_routes.bp)
    app.register_blueprint(group_routes.bp)
    app.register_blueprint(discussion_routes.bp)
