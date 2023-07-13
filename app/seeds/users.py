from app.models import db, User, environment, SCHEMA
from sqlalchemy.sql import text

def seed_users():
    trevor = User(
        username='Trevor Dobson',
        email='tdobson938@gmail.com',
        hashed_password='trevorpassword',
        first_name = 'Trevor',
        last_name = 'Dobson',
        bio = 'I mostly photograph the night sky in and around my home city of Perth in Western Australia. Occasionally I venture out to Japan and try my hand at other types of photography :-)',
        profile_photo = 'https://live.staticflickr.com/2918/buddyicons/23409752@N08_r.jpg?1400500599#23409752@N08',
        cover_photo = 'https://live.staticflickr.com/5708/coverphoto/23409752@N08_h.jpg?1480672429#23409752@N08'
        )
    klaus = User(
        username='Aerial Photohraphy',
        email='klausl509@gmail.com',
        hashed_password='klauspassword',
        first_name='Klaus',
        last_name='Leidorf',
        bio="""Klaus Leidorf: A german aerial archaeologist that likes to observe the human artifacts from a bird's eye view.
        If you want to know a little bit more about me, read this:
        www.popphoto.com/Features/Sky-s-the-Limit
        The content of these images CANNOT BE COPIED, DISTRIBUITED or PUBLISHED for any media, electronic or otherwise.
        The utilization in other web pages without the express written consent of the author is PROHIBITED. But for private purposes it will be no problem to get the permission.""",
        profile_photo='https://live.staticflickr.com/55/buddyicons/62448022@N00_r.jpg?1148663931#62448022@N00)',
        cover_photo='https://live.staticflickr.com/5443/coverphoto/62448022@N00_h.jpg?1401996965#62448022@N00)'
        )

    all_users = [trevor, klaus]

    _ = [db.session.add(user) for user in all_users]
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
