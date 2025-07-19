from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.models.wallet import Wallet
from app.models.user import User

wallet_bp = Blueprint("wallet", __name__, url_prefix="/wallet")

@wallet_bp.route("/", methods=["GET"])
@jwt_required()
def get_wallet():
    user_id = get_jwt_identity()
    user = User.query.get(user_id)

    if not user.wallet:
        return jsonify({"balance": 0, "total_earned": 0}), 200

    wallet = user.wallet
    return jsonify({
        "balance": wallet.balance,
        "total_earned": wallet.total_earned
    }), 200
