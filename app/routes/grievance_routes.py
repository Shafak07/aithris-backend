from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.extensions import db
from app.models.grievance import Grievance
from app.models.user import User

grievance_bp = Blueprint("grievance", __name__, url_prefix="/grievance")

@grievance_bp.route("/create", methods=["POST"])
@jwt_required()
def create_grievance():
    user_id = get_jwt_identity()
    data = request.get_json()

    grievance = Grievance(
        user_id=user_id,
        subject=data.get("subject"),
        description=data.get("description")
    )

    db.session.add(grievance)
    db.session.commit()
    return jsonify({"message": "Grievance created successfully"}), 201

@grievance_bp.route("/", methods=["GET"])
@jwt_required()
def list_grievances():
    user_id = get_jwt_identity()
    user = User.query.get(user_id)
    result = [
        {
            "id": g.id,
            "subject": g.subject,
            "status": g.status,
            "created_at": g.created_at
        }
        for g in user.grievances
    ]
    return jsonify(result), 200
