# app.py
from flask import Flask
from flask_jwt_extended import JWTManager
from config import Config
from models import db, init_db
from routes import register_routes
from functions.error_handler import handle_error

app = Flask(__name__)
app.config.from_object(Config)

# Initialize database
init_db(app)
jwt = JWTManager(app)

# Register blueprints
register_routes(app)

# Global error handler
app.register_error_handler(Exception, handle_error)

if __name__ == '__main__':
    app.run(debug=True)
