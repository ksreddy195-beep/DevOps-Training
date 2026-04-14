from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory storage (temporary database)
users = []

@app.route("/", methods=["GET"])
def home():
    return "API Server is running "

@app.route("/hello", methods=["GET"])
def hello():
    return jsonify({
        "message": "Hello, welcome to APIs!",
        "status": "success"
    })

# POST API
@app.route("/users", methods=["POST"])
def create_user():
    data = request.get_json()

    user = {
        "id": len(users) + 1,
        "name": data.get("name"),
        "role": data.get("role")
    }

    users.append(user)

    return jsonify({
        "message": "User created successfully",
        "user": user
    }), 201

# GET API to see created users
@app.route("/users", methods=["GET"])
def get_users():
    return jsonify(users)

if __name__ == "__main__":
    app.run(debug=True)