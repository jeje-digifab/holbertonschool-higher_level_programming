#!/usr/bin/python3
"""
This script creates a Flask API for managing user data with utility
functions for basic operations.
"""

from flask import Flask, jsonify, request

app = Flask(__name__)

users = {
    "jane": {
        "username": "jane",
        "name": "Jane",
        "age": 28,
        "city": "Los Angeles"
    },
    "john": {
        "username": "john",
        "name": "John",
        "age": 30,
        "city": "New York"
    }
}


@app.route("/")
def home():
    """
    Home route that returns a welcome message.

    Returns:
        str: A simple welcome message.
    """
    return jsonify("Welcome to the Flask API!")


@app.route("/data")
def get_usernames():
    """
    Endpoint to retrieve a list of usernames.

    Returns:
        JSON: A JSON array containing the usernames of all users.
    """
    usernames = [user["username"] for user in users.values()]
    return jsonify(usernames)


@app.route("/users/<username>")
def get_user(username):
    """
    Endpoint to retrieve detailed information about a specific user.

    Args:
        username (str): The username of the user to retrieve.

    Returns:
        JSON: A JSON object with user details if found, or an error message
        if not found.
    """
    user = users.get(username)
    if user:
        return jsonify(user), 200
    else:
        return jsonify({"error": "User not found"}), 404


@app.route("/status")
def status():
    """
    Endpoint to check the status of the API.

    Returns:
        JSON: A JSON response indicating the status.
    """
    return jsonify("OK"), 200


@app.route("/add_user", methods=['POST'])
def add_user():
    """
    Endpoint to add a new user.

    Request Body:
        JSON: A JSON object containing user data, including username, name,
        age, and city.

    Returns:
        JSON: A message indicating the result of the operation,
        including the added user or an error message.
    """
    data = request.get_json()

    if not data:
        return jsonify({'message': 'No data provided'}), 400

    username = data.get("username")
    if not username:
        return jsonify({'message': 'Username is required'}), 400

    if username in users:
        return jsonify({'error': 'User already exists',
                        'user': users[username]}), 200

    user_data = {
        "username": username,
        "name": data.get("name"),
        "age": data.get("age"),
        "city": data.get("city")
    }
    users[username] = user_data
    return jsonify({'message': 'User added', 'user': user_data}), 201


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
