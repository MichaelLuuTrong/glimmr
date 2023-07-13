from sqlalchemy.schema import Table
from .db import db, add_prefix_for_prod, environment, SCHEMA

albums_photos= Table(
    "albums_photos",
    db.Model.metadata,
    db.Column("album_id", db.ForeignKey(add_prefix_for_prod("albums.id")), primary_key=True),
    db.Column("photo_id", db.ForeignKey(add_prefix_for_prod("photos.id")), primary_key=True))

if environment == "production":
       watchlists_stocks.schema = SCHEMA
