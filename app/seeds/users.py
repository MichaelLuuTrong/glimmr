from app.models import db, User, environment, SCHEMA
from sqlalchemy.sql import text

def seed_users():
    klaus = User(
        username='Aerial Photohraphy',
        email='klausl509@gmail.com',
        password='klauspassword',
        first_name='Klaus',
        last_name='Leidorf',
        bio="""
        Klaus Leidorf: A german aerial archaeologist that likes to observe the human artifacts from a bird's eye view.
        If you want to know a little bit more about me, read this:
        www.popphoto.com/Features/Sky-s-the-Limit
        The content of these images CANNOT BE COPIED, DISTRIBUITED or PUBLISHED for any media, electronic or otherwise.
        The utilization in other web pages without the express written consent of the author is PROHIBITED. But for private purposes it will be no problem to get the permission.
        """,
        profile_photo='https://i.imgur.com/8Jm1fek.jpg',
        cover_photo='https://i.imgur.com/T43aWJr.jpg'
        )
    alexander = User(
        username='MarineBioAlex',
        email='alexsemenov523@gmail.com',
        password='alexanderpassword',
        first_name='Alexander',
        last_name='Semenov',
        bio="I’m marine biologist, specialising in invertebrate animals. Currently, I’m the Head of the Divers’ team at Moscow State University’s White Sea Biological Station where I organise and manage all sorts of underwater work. My team and I are used to diving in unfavourable and often harsh conditions, successfully conducting complex research projects. I’m a professional underwater photographer with 9 years of experience. My key specialism is scientific macrophotography in natural environments. This practice makes it possible to observe animals that cannot be properly studied under laboratory conditions, such as soft bodied planktonic organisms or stationary life forms living on the sea floor. My personal goal is to study underwater life through camera lenses and to boost people’s interest in marine biology. I do this by sharing all my finding through social media and in real life through public lectures, movies, exhibitions and media events.",
        profile_photo='https://i.imgur.com/GRofAEK.jpg',
        cover_photo='https://i.imgur.com/4Bocffa.jpg'
    )
    steve = User(
        username='TheOwlMan',
        email='stevelargeowls345@gmail.com',
        password='stevepassword',
        first_name='Steve',
        last_name='Large',
        bio="I have been interested in photography since I was a young boy many decades ago. I had a cheap box camera and would develop photos in an old closet in the basement of my parents house in Courtenay B.C. Back then we used messy chemicals and I created small negative sized contact prints in black and white. Needless to say, digital photography was all thought of as science fiction in those days. We would sometimes hear rumors of the digital technology but never dreamed that it would develop into what we see today. As a young man I upgraded to a film SLR camera which allowed me to gain more knowledge of how exposure and lighting worked in order to get good results. You couldn’t afford to take more than a few pictures at a time as everything was chemical based and very expensive to have developed. Most roles of film were a set ISO in lots of 24 or 36 photographs per role. You had to always make sure that your settings were perfect and that there was something worthwhile to shoot before pressing the shutter button. There was a period for several years where I did not do photography at all. I spent a lot of time working and involving myself in other pursuits such as amateur radio. This later developed into more modern interests like computers, the Internet, and digital multimedia not to mention getting married and raising a family. It wasn’t until my mid forties when digital photography became more mainstream that I started to get interested in photography once more.",
        profile_photo='https://i.imgur.com/Vz2yeN4.jpg',
        cover_photo='https://i.imgur.com/3rQycJo.jpg'
    )

    all_users = [klaus, alexander, steve]

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
