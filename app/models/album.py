from .db import db, environment, SCHEMA, add_prefix_for_prod
from .albums_photos import albums_photos

class Album(db.Model):
    __tablename__ = 'albums'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key = True)
    user_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod("users.id")), nullable = False)
    title = db.Column(db.String(30), nullable = False)
    description = db.Column(db.String(2000), nullable = False)

    #relationship attributes

    #album to one
    user = db.relationship("User", back_populates = "albums")

    #album to many
    photos = db.relationship("Photo", secondary = albums_photos, back_populates = "albums")

    def to_dict(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "title": self.title,
            "description": self.description
        }
