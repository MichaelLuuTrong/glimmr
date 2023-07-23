from app.models import db, User, environment, SCHEMA
from sqlalchemy.sql import text

def seed_users():
    demo = User(
        username='Demo User',
        email='demo@aa.io',
        password='password',
        first_name='Demo',
        last_name='User',
        bio="Hi! I'm a demo user and I'm exploring this website.",
        profile_photo='https://glimmr-photographs.s3.us-west-2.amazonaws.com/demo+profile+photo.jpg',
        cover_photo='https://glimmr-photographs.s3.us-west-2.amazonaws.com/demo+cover+photo.jpg'
        )

    dp = User(
        username='DP Photography',
        email='dpphotography@aa.io',
        password='password',
        first_name='Dennis',
        last_name='Polkläser',
        bio=
        """
        Dennis Polkläser, born in 1983 and based in Germany, is an award-winning photoartist and workshop educator with focus mainly on landscape photography.

        With his art and his style of photography he is always aiming to express his fascination and passion for the wild and primal regions of this planet and to capture the beauty of nature.

        Dennis preferred motives are scandinavian landscapes in combination with an expressive mood of the light and dramatic weather situation.

        He has already achieved several successes in international photography contests and his work has been published in various media.
        """,
        profile_photo='https://glimmr-photographs.s3.us-west-2.amazonaws.com/dp+profile+photo.jpg',
        cover_photo='https://glimmr-photographs.s3.us-west-2.amazonaws.com/dp+cover+photo.jpg'
        )

    jy = User(
        username='joshuay04',
        email='joshuay04@aa.io',
        password='password',
        first_name='Joshua',
        last_name='Young',
        bio=
        """
        I have always loved to travel with my family. Whether it’s a weekend road trip or a cross-country adventure, there’s nothing quite like exploring new places and creating lasting memories with the ones you love. Through my travel posts, I aim to share my favorite destinations, tips for traveling with kids, and ideas for making the most of your time on the road.
        """,
        profile_photo='https://glimmr-photographs.s3.us-west-2.amazonaws.com/joshyoung+profile+photo.jpg',
        cover_photo='https://glimmr-photographs.s3.us-west-2.amazonaws.com/joshyoung+cover+pohoto.jpg'
        )

    mc = User(
        username='michele carbone',
        email='mcarbone04@aa.io',
        password='password',
        first_name='Michele',
        last_name='Carbone',
        bio=
        """
        I am a photographer from Novara, Italia. Thank you looking at my page.
        """,
        profile_photo='https://glimmr-photographs.s3.us-west-2.amazonaws.com/michelecarbone+profile+photo.jpg',
        cover_photo='https://glimmr-photographs.s3.us-west-2.amazonaws.com/michelecarbone+cover+photo.jpg'
        )

    mj = User(
        username='Michal Jeska',
        email='mjeska@aa.io',
        password='password',
        first_name='Michal',
        last_name='Jeska',
        bio=
        """
        I'm in my 30s and work in the sports industry. I love shooting pictures with old cameras and often vintage lenses while hiking, backpacking, mountaineering, and cycling.'.
        """,
        profile_photo='https://glimmr-photographs.s3.us-west-2.amazonaws.com/michaljeska+profile+photo.jpg',
        cover_photo='https://glimmr-photographs.s3.us-west-2.amazonaws.com/michaljeska+cover+photo.jpg'
        )

    md = User(
        username="mikederrico69",
        email='mdericco04@aa.io',
        password='password',
        first_name='Mike',
        last_name="D'Errico",
        bio=
        """
        Hi everyone ! Becoming a photographer gave me an entirely new perspective on everyday life. I use photography to turn almost anything I find beautiful into a work of art. I try to use my photographic skills to creatively capture an array of subjects that ranges from landscape mood to human and animal emotion. I do this by exploring the world through my camera lens. Inspiration comes from underwater photography (scuba diving) and hiking this amazing planet.
        """,
        profile_photo='https://glimmr-photographs.s3.us-west-2.amazonaws.com/mikederrico+profile+photoi.jpg',
        cover_photo='https://glimmr-photographs.s3.us-west-2.amazonaws.com/mikederrico+cover+photo.jpg'
        )

    sm = User(
        username="smarshasm",
        email='smashasm04@aa.io',
        password='password',
        first_name='Steven',
        last_name="Marshall",
        bio=
        """
        Fortunate enough to be living at Rockpool House on the Ardnamurchan Peninsula, a wild, remote and yet beautiful place in the Scottish Highlands. Fortunate enough to have time to look at the landscape, look at the light and to really look at Scotland. And fortunate enough to be able to share images of what is a truly stunning country.
        """,
        profile_photo='https://glimmr-photographs.s3.us-west-2.amazonaws.com/stevenmarshall+profile+photo.jpg',
        cover_photo='https://glimmr-photographs.s3.us-west-2.amazonaws.com/stevenmarshall+cover+photo.jpg'
        )

    pm = User(
        username="peter manintveld",
        email='peterm@aa.io',
        password='password',
        first_name='Peter',
        last_name="Manintveld",
        bio=
        """
        Hi, I'm Peter, an amateur photographer living in the south-west of the Netherlands, and using Sony gear.
        """,
        profile_photo='https://glimmr-photographs.s3.us-west-2.amazonaws.com/petermanintveld+profile+photo.jpg',
        cover_photo='https://glimmr-photographs.s3.us-west-2.amazonaws.com/petermanintveld+cover+photo.jpg'
        )

    im = User(
        username="alma csutka",
        email='imester@aa.io',
        password='password',
        first_name='Ibolya',
        last_name="Mester",
        bio=
        """
        Hi, my dear friend, welcome to my world!

        Although I live in a town, I am a crazy nature lover! If I can, I'll run out into the meadow or the woods, away from the noise of people... If you have time, look at my photographs. I hope you'll enjoy the silence too!
        """,
        profile_photo='https://glimmr-photographs.s3.us-west-2.amazonaws.com/almacsutska+profile+photo.jpg',
        cover_photo='https://glimmr-photographs.s3.us-west-2.amazonaws.com/almacutska+cover+photo.jpg'
        )

    dl = User(
        username="valecomte20",
        email='dlacaze@aa.io',
        password='password',
        first_name='Dominique',
        last_name="Lacaze",
        bio=
        """
        I disocvered photography with a digital SLR in 2014. I'm an amateur photographer with little innate artistic ability, but I learn while traveling.
        """,
        profile_photo='https://glimmr-photographs.s3.us-west-2.amazonaws.com/dominiquelacaze+profile+photo.jpg',
        cover_photo='https://glimmr-photographs.s3.us-west-2.amazonaws.com/doiniquelacaze+cover+photo.jpg'
        )


    all_users = [demo, dp, jy, mc, mj, md, sm, pm, im, dl]

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
