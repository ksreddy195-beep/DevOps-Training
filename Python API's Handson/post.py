from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/users", methods=["POST"])
def create_user():
    data = request.get_json()

    user = {
        "name": data.get("name"),
        "role": data.get("role")
    }

    return jsonify({
        "message": "User created successfully",
        "user": user
    }), 201

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)