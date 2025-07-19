from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.extensions import db
from app.models.project import Project
from app.models.user import User
from app.schemas.project_schema import ProjectSchema

project_bp = Blueprint("project", __name__, url_prefix="/projects")

project_schema = ProjectSchema()
project_list_schema = ProjectSchema(many=True)

@project_bp.route("/", methods=["GET"])
@jwt_required()
def get_user_projects():
    user_id = get_jwt_identity()
    user = User.query.get(user_id)
    return project_list_schema.dump(user.projects), 200
