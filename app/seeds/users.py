from app.models import db, User, environment, SCHEMA
from sqlalchemy.sql import text


# Adds a demo user, you can add other users here if you want
def seed_users():
    Trevor = User(
        username='Trevor Dobson',
        email='tdobson938@gmail.com',
        password='password',
        first_name = 'Trevor',
        last_name = 'Dobson',
        bio = 'I mostly photograph the night sky in and around my home city of Perth in Western Australia. Occasionally I venture out to Japan and try my hand at other types of photography :-)',
        profile_photo = 'https://live.staticflickr.com/2918/buddyicons/23409752@N08_r.jpg?1400500599#23409752@N08',
        cover_photo = 'https://live.staticflickr.com/5708/coverphoto/23409752@N08_h.jpg?1480672429#23409752@N08'
        )

    db.session.add(Trevor)
    db.session.commit()


# Uses a raw SQL query to TRUNCATE or DELETE the users table. SQLAlchemy doesn't
# have a built in function to do this. With postgres in production TRUNCATE
# removes all the data from the table, and RESET IDENTITY resets the auto
# incrementing primary key, CASCADE deletes any dependent entities.  With
# sqlite3 in development you need to instead use DELETE to remove all data and
# it will reset the primary keys for you as well.
def undo_users():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.users RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM users"))

    db.session.commit()
