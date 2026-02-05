from flask import Blueprint, request, jsonify
from app.services.user_service import (
    create_user,
    get_all_users,
    update_user,
    delete_user
)

users_bp = Blueprint("users", __name__)

@users_bp.route("/users", methods=["POST"])
def create():
    data = request.get_json()
    if not data or "name" not in data or "email" not in data:
        return jsonify({"error": "name and email required"}), 400

    user_id = create_user(data["name"], data["email"])
    return jsonify({"message": "User created", "id": user_id}), 201


@users_bp.route("/users", methods=["GET"])
def get_users():
    return jsonify(get_all_users()), 200


@users_bp.route("/users/<int:user_id>", methods=["PUT"])
def update(user_id):
    data = request.get_json()
    if not data or "name" not in data or "email" not in data:
        return jsonify({"error": "name and email required"}), 400

    if not update_user(user_id, data["name"], data["email"]):
        return jsonify({"error": "User not found"}), 404

    return jsonify({"message": "User updated"}), 200


@users_bp.route("/users/<int:user_id>", methods=["DELETE"])
def delete(user_id):
    if not delete_user(user_id):
        return jsonify({"error": "User not found"}), 404

    return jsonify({"message": "User deleted"}), 200
