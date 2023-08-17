from flask import Blueprint
from flask_login import login_required, current_user
from ..models import db, User, Photo, Favorite
from datetime import datetime

favorite_routes = Blueprint("favorites", __name__)

#Create a Favorite by photo_id
@favorite_routes.route('/<int:photo_id>/<int:user_id>', methods=["POST"])
def post_favorite(photo_id, user_id):
    photo = Photo.query.get(photo_id)
    existing_favorite = Favorite.query.filter_by(photo_id=photo_id, user_id=user_id).first()
    if existing_favorite:
        return {'error': 'You have already favorited that photo'}
    if not photo:
        return {'error': 'That photo does not exist'}

    else:
        if current_user.is_authenticated:
            favorite = Favorite(
                user_id = user_id,
                photo_id = photo_id,
                created_at = datetime.now()
            )
            db.session.add(favorite)
            db.session.commit()
            return favorite.to_dict()

        else:
            return {'error': 'User is not logged in'}

#Get All Favorites by user_id
@favorite_routes.route('/<int:user_Id>', methods=["GET"])
def get_favorites_by_user_id(user_Id):
    favorites = Favorite.query.filter(Favorite.user_id == user_Id).all()
    return {'favorites:' : [favorite.to_dict() for favorite in favorites]}

#Delete a Favorite by photo_id
@favorite_routes.route('<int:photo_id>/<int:user_id>', methods=["DELETE"])
def delete_favorite(photo_id, user_id):
    if current_user.is_authenticated:
        favorite_to_delete = Favorite.query.filter_by(photo_id=photo_id, user_id=user_id).first()
        if not favorite_to_delete:
            return {'error': 'That favorite does not exist'}
        if favorite_to_delete.user_id == current_user.id:
            db.session.delete(favorite_to_delete)
            db.session.commit()
            return {'favorite': 'Your favorite has sucessfully been deleted'}
        else:
            return {'error': "You cannot delete someone else's favorite."}
    else:
        return {'error': 'You are not logged in.'}
