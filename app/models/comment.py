from .db import db, environment, SCHEMA, add_prefix_for_prod

class Comment(db.Model):
    __tablename__ = 'comments'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key = True)
    user_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod("users.id")), nullable = False)
    photo_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod("photos.id")), nullable = False)
    text = db.Column(db.String(500), nullable = False)
    created_at = db.Column(db.Date, nullable = False)
    updated_at = db.Column(db.Date, nullable = False)

    #relationship attributes
    user = db.relationship("User", back_populates = "comments")
    photo = db.relationship("Photo", back_populates = "comments")

    def to_dict(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "photo_id": self.photo_id,
            "text": self.text,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
            "user": self.user.to_dict(),
            "photo": self.photo
        }
