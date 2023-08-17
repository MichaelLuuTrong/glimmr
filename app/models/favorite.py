from .db import db, environment, SCHEMA, add_prefix_for_prod

class Favorite(db.Model):
    __tablename__ = 'favorites'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key = True)
    user_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod("users.id")), nullable = False)
    photo_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod("photos.id")), nullable = False)
    created_at = db.Column(db.Date, nullable = False)

    #relationship attributes

    #favorite to one
    user = db.relationship("User", back_populates = "favorites")
    photo = db.relationship("Photo", back_populates = "favorites")

    def to_dict(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "photo_id": self.photo_id,
            "created_at": self.created_at,
            "user": self.user.to_dict(),
            "photo": self.photo.to_dict(),
        }
