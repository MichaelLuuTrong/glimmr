from .db import db, environment, SCHEMA, add_prefix_for_prod
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


class User(db.Model, UserMixin):
    __tablename__ = 'users'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), nullable=False, unique=True)
    email = db.Column(db.String(30), nullable=False, unique=True)
    hashed_password = db.Column(db.String(255), nullable=False)
    first_name = db.Column(db.String(30), nullable=False)
    last_name = db.Column(db.String(30), nullable=False)
    bio = db.Column(db.String(2000))
    profile_photo = db.Column(db.String(500), nullable=False)
    cover_photo = db.Column(db.String(500), nullable=False)
    profile_photo = db.Column(db.String(500), nullable=False)
    cover_photo = db.Column(db.String(500), nullable=False)

    #relationship attributes

    #user to many
    photos = db.relationship("Photo", back_populates = "owner",
                          cascade="delete, delete-orphan")
    comments = db.relationship("Comment", back_populates = "owner",
                          cascade="delete, delete-orphan")
    favorites = db.relationship("Favorite", back_populates = "owner",
                          cascade="delete, delete-orphan")
    albums = db.relationship("Album", back_populates = "owner",
                        cascade="delete, delete-orphan")


    @property
    def password(self):
        return self.hashed_password

    @password.setter
    def password(self, password):
        self.hashed_password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'bio': self.bio,
            'profile_photo': self.profile_photo,
            'cover_photo': self.cover_photo
        }
