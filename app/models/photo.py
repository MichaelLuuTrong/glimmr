from .db import db, environment, SCHEMA, add_prefix_for_prod
from .albums_photos import albums_photos

class Photo(db.Model):
    __tablename__ = 'photos'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key = True)
    user_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod("users.id")), nullable = False)
    photo = db.Column(db.String, nullable = False)
    title = db.Column(db.String(30), nullable = False)
    description = db.Column(db.String(2000), nullable = False)
    taken_at = db.Column(db.Date, nullable = False)
    created_at = db.Column(db.Date, nullable = False)

    #relationship attributes

    #photo to one
    user = db.relationship("User", back_populates = "photos")

    #photo to many
    comments = db.relationship("Comment", back_populates = "photo",
                          cascade="delete, delete-orphan")
    favorites = db.relationship("Favorite", back_populates = "photo",
                          cascade="delete, delete-orphan")
    albums = db.relationship("Album", secondary = albums_photos, back_populates = "photos")

    def to_dict(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "photo": self.photo,
            "title": self.title,
            "description": self.description,
            "taken_at": self.taken_at,
            "created_at": self.created_at,
            "favorites_count": len(self.favorites),
            "comments_count": len(self.comments)
        }
