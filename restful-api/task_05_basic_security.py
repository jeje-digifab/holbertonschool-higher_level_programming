#!/usr/bin/python3
"""
Module to implement a Flask API with JWT and Basic Authentication.
"""

from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token, get_jwt_identity
from flask_jwt_extended import jwt_required, JWTManager
from flask_jwt_extended import get_jwt


app = Flask(__name__)
auth = HTTPBasicAuth()

# Configuration for JWT secret
app.config["JWT_SECRET_KEY"] = "secret"
jwt = JWTManager(app)

# User dictionary with hashed passwords
users = {
    "user1": {"username": "user1",
              "password": generate_password_hash("password"),
              "role": "user"},
    "admin1": {"username": "admin1",
               "password": generate_password_hash("password"),
               "role": "admin"}
}


@auth.verify_password
def verify_password(username, password):
    """
    Verify username and password.
    """
    user = users.get(username)
    if user and check_password_hash(user["password"], password):
        return username
    return None


@app.route("/basic-protected", methods=["GET"])
@auth.login_required
def set_basic_protected():
    """
    Basic Auth protected route.
    """
    return jsonify("Basic Auth: Access Granted")


@app.route("/login", methods=["POST"])
def set_login():
    """
    User login route that creates a JWT token.
    """
    username = request.json.get("username", None)

    user = users.get(username)
    if user and check_password_hash(user["password"],
                                    request.json.get("password", "")):
        access_token = create_access_token(
            identity=username, additional_claims={"role": user["role"]})
        return jsonify(access_token=access_token)
    return jsonify("401 Unauthorized response"), 401


@app.route("/jwt-protected", methods=["GET"])
@jwt_required()
def set_jwt_protected():
    """
    JWT protected route.
    """
    get_jwt_identity()
    return jsonify("JWT Auth: Access Granted"), 200


@app.route("/admin-only", methods=["GET"])
@jwt_required()
def set_admin_only():
    """
    Route accessible only to admins.
    """
    current_user_role = get_jwt()["role"]

    if current_user_role != "admin":
        return jsonify({"error": "Admin access required"}), 403
    return jsonify("Admin Access: Granted"), 200


@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    """
    Handle unauthorized error.
    """
    return jsonify({"error": "Missing or invalid token"}), 401


@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    """
    Handle invalid token error.
    """
    return jsonify({"error": "Invalid token"}), 401


@jwt.expired_token_loader
def handle_expired_token_error(err):
    """
    Handle expired token error.
    """
    return jsonify({"error": "Token has expired"}), 401


@jwt.revoked_token_loader
def handle_revoked_token_error(err):
    """
    Handle revoked token error.
    """
    return jsonify({"error": "Token has been revoked"}), 401


@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(err):
    """
    Handle fresh token required error.
    """
    return jsonify({"error": "Fresh token required"}), 401


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
