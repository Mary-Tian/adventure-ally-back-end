from flask import Blueprint, request, jsonify
from app import db
from app.models.user import User
from app.models.activity import Activity
from app.models.location import Location


activity_bp = Blueprint("activity", __name__, url_prefix="/activity")
favorite_bp = Blueprint("favorite", __name__, url_prefix="/favorite")
location_bp = Blueprint("location", __name__, url_prefix="/location")
user_bp = Blueprint("user", __name__, url_prefix="/user")

# CREATE
# Create a new user
@user_bp.route("", methods=['POST'])
def user_board():
    request_body = request.get_json()
    if "user" not in request_body or "user_name" not in request_body:
        return jsonify("Not Found"), 404

    new_user = User(owner=request_body["user"], title=request_body["user_name"])

    db.session.add(new_user)
    db.session.commit()

    return jsonify(f"{new_user.user_name} successfully created."), 201


# Create a new favorite
@favorite_bp.route("/<user_id>/favorite", methods=['POST'])
def create_favorite(user_id):
    user = User.query.get(user_id)
    if user is None:
        return jsonify("Not Found"), 404

    request_body = request.get_json()

    new_favorite = Favorite(user_id = user.id, likes_count=0)

    db.session.add(new_card)
    db.session.commit()

    return jsonify(f"{new_favorite.favorite_name} successfully created."), 201



# READ
# All favorites for a specific user
@favorite_bp.route("/<user_id>/favorite", methods=['GET'])
def retrieve_favorites(user_id):
    user = User.query.get(user_id)
    if user is None:
        return jsonify("Not Found"), 404
        
    favorites_response = [favorite.favorite_dict() for favorite in user.favorite]

    return jsonify(favorites_response), 200


@user_bp.route("", methods=["GET"])
def retrieve_users():
    users = User.query.all()
    users_response = [user.user_dict() for user in users]
    
    return jsonify(users_response), 200


# UPDATE
# Can update favorites by adding 'likes'
@favorite_bp.route("/<user_id>", methods=["PATCH"])
def update_favorite(user_id):
    favorite = Favorite.query.get(favorite_id)
    if favorite is None:
        return jsonify("Not Found"), 404

    favorite.likes_count += 1

    db.session.commit()

    return jsonify(f"{favorite.favorite_name} successfully updated. Current likes count = {favorite.likes_count}"), 200



# Delete a favorite
@favorite_bp.route("/<user_id>", methods=["DELETE"])
def delete_favorite(favorite_id):
    favorite = Favorite.query.get(favorite_id) 

    db.session.delete(favorite)
    db.session.commit()

    return jsonify(f"{favorite.favorite_name} successfully deleted.")