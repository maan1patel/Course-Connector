# functions/auth_functions.py
from models import db
from models.user import User
import jwt
from config import Config
from datetime import datetime, timedelta

def register_user(data):
    email = data.get('email')
    password = data.get('password')
    role = data.get('role', 'student')
    
    if not email or not password:
        return {"error": "Email and password are required"}
    
    if User.query.filter_by(email=email).first():
        return {"error": "Email already registered"}
    
    user = User(email=email, role=role)
    user.set_password(password)
    db.session.add(user)
    db.session.commit()
    return {"message": "User registered successfully", "user_id": user.id}

def login_user(data):
    email = data.get('email')
    password = data.get('password')
    
    if not email or not password:
        return {"error": "Email and password are required"}
    
    user = User.query.filter_by(email=email).first()
    if user and user.check_password(password):
        token = generate_jwt_token(user.id)
        return {"message": "Login successful", "token": token}
    else:
        return {"error": "Invalid email or password"}

def logout_user():
    # JWT is stateless; client can simply discard the token.
    return {"message": "Logout successful"}

def update_profile(data):
    user_id = data.get('user_id')
    if not user_id:
        return {"error": "User ID is required"}
    user = User.query.get(user_id)
    if not user:
        return {"error": "User not found"}
    
    new_email = data.get('email')
    if new_email:
        user.email = new_email
    db.session.commit()
    return {"message": "Profile updated successfully"}

def get_user_profile(user_id):
    user = User.query.get(user_id)
    if not user:
        return {"error": "User not found"}
    return {"id": user.id, "email": user.email, "role": user.role}

def generate_jwt_token(user_id):
    payload = {
        'user_id': user_id,
        'exp': datetime.utcnow() + timedelta(hours=1)
    }
    token = jwt.encode(payload, Config.SECRET_KEY, algorithm='HS256')
    return token

def verify_jwt_token(token):
    try:
        payload = jwt.decode(token, Config.SECRET_KEY, algorithms=['HS256'])
        return payload['user_id']
    except jwt.ExpiredSignatureError:
        return None
    except jwt.InvalidTokenError:
        return None

def get_db():
    from models import db  # Import inside function to avoid circular dependency
    return db
