from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory users dictionary
users = {}


@app.route("/")
def home():
    """Root endpoint"""
    return "Welcome to the Flask API!"


@app.route("/status")
def status():
    """Status endpoint"""
    return "OK"


@app.route("/data")
def data():
    """Return list of usernames"""
    return jsonify(list(users.keys()))


@app.route("/users/<username>")
def get_user(username):
    """Return user object by username"""
    if username in users:
        return jsonify(users[username])
    return jsonify({"error": "User not found"}), 404


@app.route("/add_user", methods=["POST"])
def add_user():
    """Add a new user via POST"""
    data = request.get_json()

    if not data or "username" not in data:
        return jsonify({"error": "Username is required"}), 400

    username = data["username"]
    users[username] = data
    return jsonify({"message": "User added", "user": data}), 201


if __name__ == "__main__":
    # Run Flask development server
    app.run(host="0.0.0.0", port=5000)
