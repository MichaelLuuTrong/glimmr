from flask import Blueprint
from flask_login import login_required, current_user
from ..models import db, User, Photo, Comment

photo_routes = Blueprint("photos", __name__)

#Delete Photo by photo_id
@photo_routes.route('/delete/<int:photo_id>', methods=["DELETE"])
def delete_photo_by_photo_id(photo_id):
    if current_user.is_authenticated:
        photo = Photo.query.get(photo_id)
        if not photo:
            return {'error': 'That photo does not exist'}
        if photo.user_id == current_user.id:
            db.session.delete(photo)
            db.session.commit
            return {'photo': 'Your photo has successfully been deleted.'}
        else:
            return {'error': "You cannot delete someone else's photo."}
    else:
        return {'error': 'You are not logged in.'}

#Get Photo by photo_id
@photo_routes.route('/<int:photo_id>')
def get_photo_by_id(photo_id):
    photo = Photo.query.get(photo_id)
    return photo.to_dict()

#Get All Photos by user_id
@photo_routes.route('/user/<int:user_Id>')
def get_photos_by_user_id(user_Id):
    photos = Photo.query.filter(Photo.user_id == user_Id).all()
    return {'photos:' : [photo.to_dict() for photo in photos]}

#Get All Photos
@photo_routes.route('/')
def get_all_photos():
    photos = Photo.query.all()
    for photo in photos:
        return {'photos' : [photo.to_dict() for photo in photos]}
