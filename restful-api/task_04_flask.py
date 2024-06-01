#!/usr/bin/python3

from flask import Flask, jsonify, request, abort

app = Flask(__name__)
users = {}

@app.route("/")
def home():
    return "Welcome to the Flask API!"

@app.route("/data")
def data():
    return jsonify(list(user.keys()))

@app.route("/status")
def status():
    return "OK"

@app.route("/users/<username>")
def get_user(username):
    if username not in users:
        return jsonify({"error": "User not found"}), 404
    user = users[username]
    user["username"] = username
    return jsonify(user)


@app.route("/add_user", methods=["POST"])
def add_user():
    user_data = request.json
    username = user_data.get("username")
    if not username:
        return jsonify({"error": "Username is required"}), 400
    if username in users:
        return jsonify({"error": "User already exists"}), 400
    users[username] = user_data
    return jsonify({"message": "User added", "user": user_data})

if __name__ == "__main__":
    app.run(host="localhost", port=5000, debug=True)
