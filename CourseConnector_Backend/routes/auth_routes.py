# routes/auth_routes.py
from flask import Blueprint, request
from functions.auth_functions import register_user, login_user

bp = Blueprint("auth", __name__, url_prefix="/auth")

@bp.route('/register', methods=['POST'])
def register():
    data = request.json
    return register_user(data['email'], data['password'], data.get('role', 'student'))

@bp.route('/login', methods=['POST'])
def login():
    data = request.json
    return login_user(data['email'], data['password'])
