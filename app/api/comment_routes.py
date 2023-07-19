from flask import Blueprint
from flask_login import login_required, current_user
from ..models import db, User, Photo, Comment
from app.forms.comment_form import CommentForm
from datetime import datetime

comment_routes = Blueprint("comments", __name__)

#Post A Comment By photo_id
@comment_routes.route('/<int:photo_id>/<int:user_id>', methods=["POST"])
def post_comment(photo_id, user_id):
    photo = Photo.query.get(photo_id)
    if not photo:
        return {'error': 'That photo does not exist'}
    else:
        if current_user.is_authenticated:
            if user_id == current_user.id:
                form = CommentForm()
                comment = Comment(
                    user_id = user_id,
                    photo_id = photo_id,
                    text = form.data['text'],
                    created_at = datetime.now(),
                    updated_at = datetime.now()
                )
                db.session.add(comment)
                db.session.commit()
                return comment.to_dict()
            else:
                return {'error': "You cannot post a comment as someone else."}
        else:
            return {'error': 'You are not logged in.'}

#Get Comment by comment_id
@comment_routes.route('/comment/<int:comment_id>')
def get_comment_by_comment_id(comment_id):
    comment = Comment.query.get(comment_id)
    if not comment:
        return {'error': 'That comment does not exist'}
    else:
        return comment.to_dict()


#Get All Comments by photo_id
@comment_routes.route('/<int:photo_id>')
def get_comment_by_photo_id(photo_id):
    photo = Photo.query.get(photo_id)
    if not photo:
        return {'error': 'That photo does not exist'}
    else:
        comments = Comment.query.filter(Comment.photo_id == photo_id).all()
        return {'comments': [comment.to_dict() for comment in comments]}

#Edit a Comment by comment_id
@comment_routes.route('/<int:comment_id>', methods=["PATCH"])
def edit_comment_by_comment_id(comment_id):
    if current_user.is_authenticated:
        form = CommentForm()
        comment_to_edit = Comment.query.get(comment_id)
        if not comment_to_edit:
            return {'error': 'That comment does not exist'}
        if comment_to_edit.user_id == current_user.id:
            comment_to_edit.text = form.data['text']
            comment_to_edit.updated_at = datetime.now()
            db.session.add(comment_to_edit)
            db.session.commit()
            return comment_to_edit.to_dict()
        else:
            return {'error': "You cannot edit someone else's comment."}
    else:
        return {'error': 'You are not logged in.'}

#Delete Comment by comment_id
@comment_routes.route('/<int:comment_id>', methods=["DELETE"])
def delete_comment_by_id(comment_id):
    if current_user.is_authenticated:
        comment_to_delete = Comment.query.get(comment_id)
        if not comment_to_delete:
            return {'error': 'That comment does not exist'}
        if comment_to_delete.user_id == current_user.id:
            db.session.delete(comment_to_delete)
            db.session.commit()
            return {'comment': 'Your comment has successfully been deleted.'}
        else:
            return {'error': "You cannot delete someone else's comment."}
    else:
        return {'error': 'You are not logged in.'}
