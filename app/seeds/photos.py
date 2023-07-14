from app.models import db, Photo, environment, SCHEMA
from sqlalchemy.sql import text
from datetime import datetime

def convert_date(input_date):
    # Map month names to their corresponding numbers
    month_map = {
        "January": 1,
        "February": 2,
        "March": 3,
        "April": 4,
        "May": 5,
        "June": 6,
        "July": 7,
        "August": 8,
        "September": 9,
        "October": 10,
        "November": 11,
        "December": 12
    }

    # Split the input date into month, day, and year
    date_parts = input_date.split(" ")
    month = month_map[date_parts[0]]
    day = int(date_parts[1].rstrip(","))
    year = int(date_parts[2])

    # Create a datetime object with the date components
    output_date = datetime(year, month, day)

    return output_date

def seed_photos():
    #1
    klaus1 = Photo(
        user_id=1,
        photo='https://i.imgur.com/4rvoIwH.jpg',
        title='Ascending Mist',
        description='Luftbild vom Großen Arber, Blick vom Osten',
        taken_at=convert_date("October 11, 2010"),
        created_at=convert_date("October 28, 2010")
    )
    klaus2 = Photo(
        #2
        user_id=1,
        photo='https://i.imgur.com/zKYRwGp.jpg',
        title='Autumn around Chinese Tower',
        description='Luftbild vom herbstlich bunt gefärbten Englischen Garten am Chinesischen Turm in München',
        taken_at=convert_date("October 27, 2010"),
        created_at=convert_date("October 27, 2011")
    )
    klaus3 = Photo(
        #3
        user_id=1,
        photo='https://i.imgur.com/Gja2Stv.jpg',
        title='Brightly Coloured Balloon',
        description='Luftbild von einem bunten Heißluftballon',
        taken_at=convert_date("September 5, 2011"),
        created_at=convert_date("September 5, 2011")
    )
    klaus4 = Photo(
        #4
        user_id=1,
        photo='https://i.imgur.com/Y1sv073.jpg',
        title='Lonely Planet',
        description='Luftbild von einem kleinen Häuschen auf einem Trinkwasserbrunnen bei Sassanfahrt',
        taken_at=convert_date("June 23, 2010"),
        created_at=convert_date("July 6, 2010")
    )
    klaus5 = Photo(
        #5
        user_id=1,
        photo='https://i.imgur.com/9u0RufG.jpg',
        title='Trees in a Row - 03',
        description='Luftbild von Lindenbaumreihen am Neuen Südfriedhof in München-Perlach',
        taken_at=convert_date("April 10, 2019"),
        created_at=convert_date("April 12, 2019")
    )
    klaus6 = Photo(
        #6
        user_id=1,
        photo='https://i.imgur.com/uzpAtLm.jpg',
        title='Trees in a Row - 15',
        description='Luftbild von den Lindenbaumreihen im Winter auf dem Südfriedhof in München-Perlach',
        taken_at=convert_date("February 18, 2019"),
        created_at=convert_date("February 20, 2019")
    )
    klaus7 = Photo(
        #7
        user_id=1,
        photo='https://i.imgur.com/QYdemjc.jpg',
        title='Trees in a Row - 01',
        description='Luftbild von einer Reihe schattenwerfender Kirschbäume am Feldweg',
        taken_at=convert_date("December 16, 2013"),
        created_at=convert_date("December 19, 2017")
    )
    alexander1 = Photo(
        #8
        user_id=2,
        photo='https://i.imgur.com/qmgGsm5.jpg',
        title='Some shrimp on Crossaster pappusus',
        description='Taken with Nikon D850',
        taken_at=convert_date("September 17, 2018"),
        created_at=convert_date("October 8, 2021")
    )
    alexander2 = Photo(
        #9
        user_id=2,
        photo='https://i.imgur.com/B3WqOKh.jpg',
        title='Staurozoika',
        description='Unidentified staurozoan jellyfish from Northern Kuril Islands, Northern pacific.',
        taken_at=convert_date("January 7, 2023"),
        created_at=convert_date("January 7, 2023")
    )
    alexander3 = Photo(
        #10
        user_id=2,
        photo='https://i.imgur.com/PBkN1Ts.jpg',
        title='Beroe cucumis with a mouth wide open',
        description='Taken with Nikon D850',
        taken_at=convert_date("April 6, 2019"),
        created_at=convert_date("January 17, 2023")
    )
    alexander4 = Photo(
        #11
        user_id=2,
        photo='https://i.imgur.com/uyBKyH1.jpg',
        title='Crossaster papposus skin',
        description='taken with Hasselblad X1D II 50C',
        taken_at=convert_date("June 7, 2023"),
        created_at=convert_date("June 21, 2023")
    )
    steve1 = Photo(
        #12
        user_id=3,
        photo='https://i.imgur.com/SLwAWVa.jpg',
        title='Sunny Day Mandarin (Mandarin Duck)',
        description='The sun was a bit harsh today but I did my best to avoid the shadows. Got some pretty good detail as the mandarin came in really close this time.',
        taken_at=convert_date("March 29, 2020"),
        created_at=convert_date("March 30, 2020")

    )
    steve2 = Photo(
        #13
        user_id=3,
        photo='https://i.imgur.com/hpipO2O.jpg',
        title='Mandarin In Flight (Mandarin Duck)',
        description='Took this one from about 200 feet with 1200 mm. Just a quick grab as they burst off of the water. Here is the mandarin male flying with his female wood duck mate.',
        taken_at=convert_date("March 29, 2020"),
        created_at=convert_date("March 31, 2020")
    )
    steve3 = Photo(
        #14
        user_id=3,
        photo='https://i.imgur.com/UPvxtHo.jpg',
        title='Bird On a Wire (Northern Hawk Owl)',
        description="OK, don't get excited! This is not from any of my recent images. I have been getting a few inquiries lately from my buddies that may have not been around or did not do bird photos when the hawk owl was in Nanaimo. I also wanted to start a new album for my owl section on them. My gear is a lot better these days than it was in 2009 when this was taken. However, I do have a few shots that will probably benefit from some of our fine new technology and I have decided to re-work a few hawk owl photos. Don't be too surprised if you see some of them mixed in with my short-ear stuff as I go through the old images and rejuvenate them.",
        taken_at=convert_date("February 8, 2009"),
        created_at=convert_date("November 26, 2017")
    )
    steve4 = Photo(
        #15
        user_id=3,
        photo='https://i.imgur.com/oHN6UaM.jpg',
        title='Right At Eye Level (Northern Hawk Owl)',
        description='I was walking down a forest road by the edge of a field when my phone rang. It was my buddy Dave Pley. As I walked and talked I just happened to look over to my left and there was this hawk owl perched no more than five feet up and about fifteen feet away. Needless to say I told Dave that I would call him back later :-)',
        taken_at=convert_date("February 26, 2021"),
        created_at=convert_date("March 21, 2021")
    )

    all_photos = [klaus1, klaus2, klaus3, klaus4, klaus5,
                  klaus6, klaus7, alexander1, alexander2,
                  alexander3, alexander4, steve1, steve2,
                  steve3, steve4]

    _ = [db.session.add(photo) for photo in all_photos]
    db.session.commit()


# Uses a raw SQL query to TRUNCATE or DELETE the photos table. SQLAlchemy doesn't
# have a built in function to do this. With postgres in production TRUNCATE
# removes all the data from the table, and RESET IDENTITY resets the auto
# incrementing primary key, CASCADE deletes any dependent entities.  With
# sqlite3 in development you need to instead use DELETE to remove all data and
# it will reset the primary keys for you as well.
def undo_photos():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.photos RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM photos"))

    db.session.commit()
