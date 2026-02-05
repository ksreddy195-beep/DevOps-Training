# Import Flask class to create the app
# Import jsonify to convert Python data to JSON response
# Import request to read incoming request data (POST, PUT, etc.)
from flask import Flask, jsonify, request

# Create a Flask application instance
# _name_ helps Flask know where the app is located
app = Flask(__name__)

# In-memory storage (acts like a temporary database)
# Data will be lost when the server restarts
users = []

# -------------------- HOME API --------------------
# Route for the root URL "/"
# Accepts only GET requests
@app.route("/", methods=["GET"])
def home():
    # Returns a simple text response
    return "API Server is running "

# -------------------- HELLO API --------------------
# Route "/hello"
# Used to test JSON response
@app.route("/hello", methods=["GET"])
def hello():
    # jsonify converts Python dict into JSON format
    return jsonify({
        "message": "Hello, welcome to APIs!",
        "status": "success"
    })

# -------------------- CREATE USER (POST) --------------------
# Route "/users"
# Accepts POST requests to create a new user
@app.route("/users", methods=["POST"])
def create_user():
    # Read JSON data sent in the request body
    data = request.get_json()

    # Create a user dictionary
    # id is auto-generated using current length of users list
    user = {
        "id": len(users) + 1,
        "name": data.get("name"),   # Get name from request JSON
        "role": data.get("role")    # Get role from request JSON
    }

    # Add the new user to the users list
    users.append(user)

    # Return success message with created user
    # 201 = HTTP status code for resource created
    return jsonify({
        "message": "User created successfully",
        "user": user
    }), 201

# -------------------- GET ALL USERS --------------------
# Route "/users"
# Accepts GET requests to fetch all users
@app.route("/users", methods=["GET"])
def get_users():
    # Return all users as JSON
    return jsonify(users)

# -------------------- DELETE USER --------------------
# Route "/delete_user/<user_id>"
# <int:user_id> means user_id must be an integer
@app.route("/delete_user/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    # Use global keyword to modify the global users list
    global users

    # Remove the user whose id matches user_id
    users = [user for user in users if user["id"] != user_id]

    # Return success response
    return jsonify({
        "message": f"User with id {user_id} deleted successfully",
        "status": "success"
    })

# -------------------- UPDATE USER --------------------
# Route "/update_user/<user_id>"
# Accepts PUT requests to update user details
@app.route("/update_user/<int:user_id>", methods=["PUT"])
def update_user(user_id):
    # Read JSON data from request body
    data = request.get_json()

    # Loop through users list
    for user in users:
        # Check if user id matches
        if user["id"] == user_id:
            # Update name if provided, else keep old value
            user["name"] = data.get("name", user["name"])

            # Update role if provided, else keep old value
            user["role"] = data.get("role", user["role"])

            # Return success response
            return jsonify({
                "message": f"User with id {user_id} updated successfully",
                "user": user
            })

    # If user is not found, return error message
    return jsonify({
        "message": f"User with id {user_id} not found",
        "status": "error"
    }), 404

# -------------------- RUN SERVER --------------------
# Run the Flask app only if this file is executed directly
if __name__ == "_main_":
    # debug=True enables auto-reload and detailed error messages
    app.run(debug=True)