from flask import Blueprint
from flask_login import login_required, current_user
from ..models import db, User, Photo
from app.forms.photo_form import PhotoForm
from datetime import datetime
from app.api.AWS_helpers import (upload_file_to_s3, get_unique_filename)

photo_routes = Blueprint("photos", __name__)

#Post A Photo
@photo_routes.route('/<int:user_Id>/photos', methods=["POST"])
def post_photo(user_Id):
    if current_user.is_authenticated:
        if current_user.id == user_Id:
            form = PhotoForm()
            photo = form.data['photo']
            photo.filename = get_unique_filename(photo.filename)
            upload = upload_file_to_s3(photo)

            if "url" not in upload:
                return {Error: "Upload Error"}

            new_photo = Photo(
                user_id = user_Id,
                photo = upload["url"],
                title = form.data['title'],
                description = form.data['description'],
                taken_at = form.data['taken_at'],
                created_at = datetime.now()
            )
            db.session.add(new_photo)
            db.session.commit()
            return new_photo.to_dict()
        else:
            return {'error': "You cannot post a photo to someone else's account"}
    else:
        return {'error': 'You are not logged in.'}

#Get Photo by photo_id
@photo_routes.route('/<int:photo_id>')
def get_photo_by_id(photo_id):
    photo = Photo.query.get(photo_id)
    if not photo:
        return {'error': 'That photo does not exist'}
    else:
        return photo.to_dict()

#Get All Photos by user_Id
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

#Edit a Photo by photo_id
@photo_routes.route('/<int:photo_id>', methods=["PATCH"])
def update_photo_by_photo_id(photo_id):
    if current_user.is_authenticated:
        form = PhotoForm()
        photo_to_update = Photo.query.get(photo_id)
        if not photo_to_update:
            return {'error': 'That photo does not exist'}

        if photo_to_update.user_id == current_user.id:
            if form.data['photo']:
                photo = form.data['photo']
                photo.filename = get_unique_filename(photo.filename)
                upload = upload_file_to_s3(photo)

                if "url" not in upload:
                    return {Error: "Upload Error"}
                photo_to_update.photo = upload["url"]

            photo_to_update.title = form.data['title']
            photo_to_update.description = form.data['description']
            photo_to_update.taken_at = form.data['taken_at']
            db.session.commit()
            return photo_to_update.to_dict()
        else:
            return {'error': "You cannot edit someone else's photo."}
    else:
        return {'error': 'You are not logged in.'}

#Delete Photo by photo_id
@photo_routes.route('/<int:photo_id>', methods=["DELETE"])
def delete_photo_by_photo_id(photo_id):
    if current_user.is_authenticated:
        photo_to_delete = Photo.query.get(photo_id)
        if not photo_to_delete:
            return {'error': 'That photo does not exist'}
        if photo_to_delete.user_id == current_user.id:
            db.session.delete(photo_to_delete)
            db.session.commit()
            return {'photo': 'Your photo has successfully been deleted.'}
        else:
            return {'error': "You cannot delete someone else's photo."}
    else:
        return {'error': 'You are not logged in.'}
