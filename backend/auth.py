import jwt
import datetime
from functools import wraps
from flask import request, jsonify
import json
import os

# Secret key for encoding/decoding JWT
SECRET_KEY = os.environ.get("SECRET_KEY", "supersecretkey")

# Load users from JSON file
def load_users():
    with open("users.json") as f:
        data = json.load(f)
    return data["users"]

# Authenticate user and return token
def authenticate(auth_data):
    username = auth_data.get("username")
    password = auth_data.get("password")

    users = load_users()
    for user in users:
        if user["username"] == username and user["password"] == password:
            token = jwt.encode({
                "username": username,
                "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=1)
            }, SECRET_KEY, algorithm="HS256")
            return token

    return None

# Decorator to protect routes
def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None

        if "Authorization" in request.headers:
            token = request.headers["Authorization"].split(" ")[-1]

        if not token:
            return jsonify({"message": "Token is missing!"}), 401

        try:
            data = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
            current_user = data["username"]
        except jwt.ExpiredSignatureError:
            return jsonify({"message": "Token expired!"}), 401
        except jwt.InvalidTokenError:
            return jsonify({"message": "Invalid token!"}), 401

        return f(*args, **kwargs)

    return decorated
