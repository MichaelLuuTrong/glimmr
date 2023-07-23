from app.models import db, Photo, environment, SCHEMA
from sqlalchemy.sql import text
from datetime import datetime

def seed_photos():
    demo1 = Photo(
        user_id=1,
        photo='https://glimmr-photographs.s3.us-west-2.amazonaws.com/glimmrseederphotos/demo/demo1.jpg',
        title='Emporia',
        description="The amazing architecture of Emporia, one of Scandinavia's largest shopping malls.",
        taken_at=datetime(2021, 8, 24),
        created_at=datetime(2021, 8, 15)
    )
    demo2 = Photo(
        user_id=1,
        photo='https://glimmr-photographs.s3.us-west-2.amazonaws.com/glimmrseederphotos/demo/demo2.jpg',
        title='Suogo de Fouzargo/Ju de Falzares',
        description='Iconic mountain pass of the Dolomites, including a sight of the Church and the Sass de Stria.',
        taken_at=datetime(2019, 4, 19),
        created_at=datetime(2019, 6, 22)
    )

    demo3 = Photo(
        user_id=1,
        photo='https://glimmr-photographs.s3.us-west-2.amazonaws.com/glimmrseederphotos/demo/demo3.jpg',
        title='Faggeta del Cimino',
        description='Summer is starting to fade. Autumn is on the way...',
        taken_at=datetime(2018, 11, 17),
        created_at=datetime(2022, 7, 13)
    )

    demo4 = Photo(
        user_id=1,
        photo='https://glimmr-photographs.s3.us-west-2.amazonaws.com/glimmrseederphotos/demo/demo4.jpg',
        title='Endless Stairs',
        description='Taken in Antrodoco, Latium, Italy.',
        taken_at=datetime(2023, 5, 20),
        created_at=datetime(2023, 6, 13)
    )

    demo5 = Photo(
        user_id=1,
        photo='https://glimmr-photographs.s3.us-west-2.amazonaws.com/glimmrseederphotos/demo/demo5.jpg',
        title='Terni',
        description='The more I wander around Terni, the more my love for this city grows!',
        taken_at=datetime(2022, 6, 1),
        created_at=datetime(2022, 9, 30)
    )

    demo6 = Photo(
        user_id=1,
        photo='https://glimmr-photographs.s3.us-west-2.amazonaws.com/glimmrseederphotos/demo/demo6.jpg',
        title='Malmö',
        description='Walking through Kalendagatan, towards majestic sights.',
        taken_at=datetime(2021, 8, 15),
        created_at=datetime(2022, 11, 3)
    )

    demo7 = Photo(
        user_id=1,
        photo='https://glimmr-photographs.s3.us-west-2.amazonaws.com/glimmrseederphotos/demo/demo7.jpg',
        title='Civita di Bagnoregio',
        description='The motorcycle, the bike and the bell tower all made this alley quite interesting.',
        taken_at=datetime(2021, 7, 3),
        created_at=datetime(2022, 12, 26)
    )

    demo8 = Photo(
        user_id=1,
        photo='https://glimmr-photographs.s3.us-west-2.amazonaws.com/glimmrseederphotos/demo/demo8.jpg',
        title='Giardino di Ninfa',
        description="A relaxing view while approaching the garden's exit.",
        taken_at=datetime(2021, 7, 17),
        created_at=datetime(2022, 8, 28)
    )

    demo9 = Photo(
        user_id=1,
        photo='https://glimmr-photographs.s3.us-west-2.amazonaws.com/glimmrseederphotos/demo/demo9.jpg',
        title='Stroncone',
        description='Night and day, still alway gorgeous.',
        taken_at=datetime(2022, 10, 28),
        created_at=datetime(2023, 1, 29)
    )

    demo10 = Photo(
        user_id=1,
        photo='https://glimmr-photographs.s3.us-west-2.amazonaws.com/glimmrseederphotos/demo/demo10.jpg',
        title='A Rare Snowfall',
        description='Taken in Portuense, Rome, Latium',
        taken_at=datetime(2023, 2, 26),
        created_at=datetime(2023, 4, 19)
    )

    demo11 = Photo(
        user_id=1,
        photo='https://glimmr-photographs.s3.us-west-2.amazonaws.com/glimmrseederphotos/demo/demo11.jpg',
        title='Lost in the Setting Sun',
        description='Taken near the Roman catholic diocese of Terni, Umbria',
        taken_at=datetime(2023, 4, 3),
        created_at=datetime(2023, 4, 3)
    )

    dp1 = Photo(
        user_id=2,
        photo='https://glimmr-photographs.s3.us-west-2.amazonaws.com/glimmrseederphotos/dp/dp1.jpg',
        title='Morningrise',
        description="Dolomites, Italy, July 2018",
        taken_at=datetime(2018, 8, 7),
        created_at=datetime(2018, 8, 7)
    )

    dp2 = Photo(
        user_id=2,
        photo='https://glimmr-photographs.s3.us-west-2.amazonaws.com/glimmrseederphotos/dp/dp2.jpg',
        title='Red Carpet',
        description="Camera: Canon Eos 5 Ds R",
        taken_at=datetime(2019, 4, 20),
        created_at=datetime(2023, 4, 3)
    )

    dp3 = Photo(
        user_id=2,
        photo='https://glimmr-photographs.s3.us-west-2.amazonaws.com/glimmrseederphotos/dp/dp3.jpg',
        title='Seiser Alm',
        description="Dolomites, Italy, October 2017",
        taken_at=datetime(2018, 6, 23),
        created_at=datetime(2018, 6, 23)
    )

    dp4 = Photo(
        user_id=2,
        photo='https://glimmr-photographs.s3.us-west-2.amazonaws.com/glimmrseederphotos/dp/dp4.jpg',
        title='A Peaceful Morning',
        description="Bavaria, Germany, July 2022",
        taken_at=datetime(2022, 7, 8),
        created_at=datetime(2022, 8, 3)
    )

    dp5 = Photo(
        user_id=2,
        photo='https://glimmr-photographs.s3.us-west-2.amazonaws.com/glimmrseederphotos/dp/dp5.jpg',
        title='Primeval',
        description="Iceland, Highlands",
        taken_at=datetime(2014, 7, 26),
        created_at=datetime(2019, 12, 26)
    )

    dp6 = Photo(
        user_id=2,
        photo='https://glimmr-photographs.s3.us-west-2.amazonaws.com/glimmrseederphotos/dp/dp6.jpg',
        title='The Arrival',
        description="...deep in the misty woods of Germany",
        taken_at=datetime(2020, 11, 7),
        created_at=datetime(2020, 11, 7)
    )

    dp7 = Photo(
        user_id=2,
        photo='https://glimmr-photographs.s3.us-west-2.amazonaws.com/glimmrseederphotos/dp/dp7.jpg',
        title='The Dark Fortress',
        description="Dolomites, Italy, July 2018",
        taken_at=datetime(2018, 7, 8),
        created_at=datetime(2019, 8, 4)
    )

    dp8 = Photo(
        user_id=2,
        photo='https://glimmr-photographs.s3.us-west-2.amazonaws.com/glimmrseederphotos/dp/dp8.jpg',
        title='Evanescence',
        description="For an upcoming project",
        taken_at=datetime(2013, 4, 3),
        created_at=datetime(2021, 1, 18)
    )

    dp9 = Photo(
        user_id=2,
        photo='https://glimmr-photographs.s3.us-west-2.amazonaws.com/glimmrseederphotos/dp/dp9.jpg',
        title='Breath of Autumn',
        description="Bavaria, October 2021",
        taken_at=datetime(2021, 10, 21),
        created_at=datetime(2021, 10, 30)
    )

    dp10 = Photo(
        user_id=2,
        photo='https://glimmr-photographs.s3.us-west-2.amazonaws.com/glimmrseederphotos/dp/dp10.jpg',
        title='The Art of Nature',
        description="Iceland, 2021",
        taken_at=datetime(2021, 5, 3),
        created_at=datetime(2021, 5, 21)
    )

    dp11 = Photo(
        user_id=2,
        photo='https://glimmr-photographs.s3.us-west-2.amazonaws.com/glimmrseederphotos/dp/dp11.jpg',
        title='Dark Glacier',
        description="Alps, 2020",
        taken_at=datetime(2020, 12, 13),
        created_at=datetime(2020, 12, 20)
    )

    dp12 = Photo(
        user_id=2,
        photo='https://glimmr-photographs.s3.us-west-2.amazonaws.com/glimmrseederphotos/dp/dp12.jpg',
        title='The Beauty of Bavaria',
        description="Bavaria, July 2022",
        taken_at=datetime(2022, 7, 24),
        created_at=datetime(2023, 3, 13)
    )

    dp13 = Photo(
        user_id=2,
        photo='https://glimmr-photographs.s3.us-west-2.amazonaws.com/glimmrseederphotos/dp/dp13.jpg',
        title='Seceda',
        description="Dolomites, Italy, July 2018",
        taken_at=datetime(2018, 7, 12),
        created_at=datetime(2018, 8, 30)
    )

    dp14 = Photo(
        user_id=2,
        photo='https://glimmr-photographs.s3.us-west-2.amazonaws.com/glimmrseederphotos/dp/dp14.jpg',
        title='Otherworld',
        description="Mullerthal, 2020",
        taken_at=datetime(2020, 3, 15),
        created_at=datetime(2020, 5, 28)
    )

    dp15 = Photo(
        user_id=2,
        photo='https://glimmr-photographs.s3.us-west-2.amazonaws.com/glimmrseederphotos/dp/dp15.jpg',
        title="Eagle's View",
        description="Lofoten, Northern Norway, September 2022",
        taken_at=datetime(2022, 9, 13),
        created_at=datetime(2023, 2, 5)
    )

    jy1 = Photo(
        user_id=3,
        photo='https://glimmr-photographs.s3.us-west-2.amazonaws.com/glimmrseederphotos/jy/jy1.jpg',
        title="Paris at Night",
        description="Could there be a more beautiful city than Paris at Night?",
        taken_at=datetime(2014, 8, 10),
        created_at=datetime(2015, 1, 22)
    )

    jy2 = Photo(
        user_id=3,
        photo='https://glimmr-photographs.s3.us-west-2.amazonaws.com/glimmrseederphotos/jy/jy2.jpg',
        title="Arches Sunset Balanced Rock",
        description="What a beautiful park! Arches and Utah in general have caught my attention, this is by far one of the most fantastic places on earth. So many rock formations and so much light. This picture is taken from an easy vantage point, no difficult hike, the beauty is overflowing and accessible here!",
        taken_at=datetime(2021, 5, 4),
        created_at=datetime(2021, 5, 6)
    )
    jy3 = Photo(
        user_id=3,
        photo='https://glimmr-photographs.s3.us-west-2.amazonaws.com/glimmrseederphotos/jy/jy3.jpg',
        title="Brrr... It's Cold at the Grand Haven Lighthouse",
        description="Visiting the Grand Haven Lighthouse in the wintertime can be a bit of a challenge, especially with three kids in tow. But let me tell you, it’s worth it! The chilly weather only adds to the beauty of this historic landmark, and the kids had a blast despite the frigid temperatures.",
        taken_at=datetime(2023, 2, 4),
        created_at=datetime(2023, 2, 23)
    )

    jy4 = Photo(
        user_id=3,
        photo='https://glimmr-photographs.s3.us-west-2.amazonaws.com/glimmrseederphotos/jy/jy4.jpg',
        title="A Bruges Sunset",
        description="To enjoy an amazing sunset, travel to Bruges, order a local beer, and grab a waffle. Enjoy with chocolate.",
        taken_at=datetime(2014, 8, 7),
        created_at=datetime(2015, 2, 12)
    )

    jy5 = Photo(
        user_id=3,
        photo='https://glimmr-photographs.s3.us-west-2.amazonaws.com/glimmrseederphotos/jy/jy5.jpg',
        title="Detroit at Night",
        description="Detroit is making a come back. After ice skating at Campus Martias, it is safe to take a walk and see the glory of Detroit.",
        taken_at=datetime(2015, 1, 31),
        created_at=datetime(2015, 2, 2)
    )

    jy6 = Photo(
        user_id=3,
        photo='https://glimmr-photographs.s3.us-west-2.amazonaws.com/glimmrseederphotos/jy/jy6.jpg',
        title="Black Sands of Ireland",
        description="Do not turn your back to this magnificent beach, tides are fast and powerful! Beautiful storm with wonderful rock formations!",
        taken_at=datetime(2017, 5, 10),
        created_at=datetime(2022, 6, 29)
    )

    jy7 = Photo(
        user_id=3,
        photo='https://glimmr-photographs.s3.us-west-2.amazonaws.com/glimmrseederphotos/jy/jy7.jpg',
        title="Observing the Sunset",
        description="After a 3 mile round trip hike, Big Sable is a stunning lighthouse with fantastic views. Stay for the evening's prime event!",
        taken_at=datetime(2022, 7, 8),
        created_at=datetime(2022, 7, 18)
    )

    jy8 = Photo(
        user_id=3,
        photo='https://glimmr-photographs.s3.us-west-2.amazonaws.com/glimmrseederphotos/jy/jy8.jpg',
        title="Route de Paris",
        description="Take a carriage to the top of the city, and wait for the last light of the evening. This will prove to be a most rewarding experience.",
        taken_at=datetime(2014, 8, 2),
        created_at=datetime(2015, 1, 28)
    )

    jy9 = Photo(
        user_id=3,
        photo='https://glimmr-photographs.s3.us-west-2.amazonaws.com/glimmrseederphotos/jy/jy9.jpg',
        title="Michigan Shoreline",
        description="There is no place more beautiful than the miles of shoreline in Michigan. The great lakes are are worth visiting. This is Lake Michigan, near Manistee at Orchard Beach State Park.",
        taken_at=datetime(2014, 8, 23),
        created_at=datetime(2015, 1, 16)
    )

    jy10 = Photo(
        user_id=3,
        photo='https://glimmr-photographs.s3.us-west-2.amazonaws.com/glimmrseederphotos/jy/jy10.jpg',
        title="Sunset in Paris",
        description="Walking through the Tuileries Garden in the evening. The sunset is always stunning.",
        taken_at=datetime(2014, 8, 9),
        created_at=datetime(2015, 1, 26)
    )

    jy11 = Photo(
        user_id=3,
        photo='https://glimmr-photographs.s3.us-west-2.amazonaws.com/glimmrseederphotos/jy/jy11.jpg',
        title="Painting with Leaves",
        description="Grand Ledge Michigan offers some of the best autumn views!",
        taken_at=datetime(2020, 10, 11),
        created_at=datetime(2020, 10, 18)
    )

    mc1 = Photo(
        user_id=4,
        photo='https://glimmr-photographs.s3.us-west-2.amazonaws.com/glimmrseederphotos/mc/mc1.jpg',
        title="Autumn Again",
        description="Taken with Sony ILCE-6000",
        taken_at=datetime(2019, 11, 10),
        created_at=datetime(2020, 12, 22)
    )

    mc2 = Photo(
        user_id=4,
        photo='https://glimmr-photographs.s3.us-west-2.amazonaws.com/glimmrseederphotos/mc/mc2.jpg',
        title="Italian Landscape",
        description="Heavenly clouds.",
        taken_at=datetime(2022, 3, 20),
        created_at=datetime(2022, 3, 20)
    )

    mc3 = Photo(
        user_id=4,
        photo='https://glimmr-photographs.s3.us-west-2.amazonaws.com/glimmrseederphotos/mc/mc3.jpg',
        title="Verso L'Autunno",
        description="Taken with Sony ILCE-6000",
        taken_at=datetime(2021, 9, 15),
        created_at=datetime(2021, 9, 22)
    )

    mc4 = Photo(
        user_id=4,
        photo='https://glimmr-photographs.s3.us-west-2.amazonaws.com/glimmrseederphotos/mc/mc4.jpg',
        title="Mountains",
        description="taken with Sony ILCE-6000",
        taken_at=datetime(2020, 1, 5),
        created_at=datetime(2021, 1, 8)
    )

    mc5 = Photo(
        user_id=4,
        photo='https://glimmr-photographs.s3.us-west-2.amazonaws.com/glimmrseederphotos/mc/mc5.jpg',
        title="Il Borgo Vecchio Al Tramonto",
        description="Taken with HUAWEI ELS-NX9",
        taken_at=datetime(2021, 9, 1),
        created_at=datetime(2021, 9, 7)
    )

    mc6 = Photo(
        user_id=4,
        photo='https://glimmr-photographs.s3.us-west-2.amazonaws.com/glimmrseederphotos/mc/mc6.jpg',
        title="Sunrise in the Countryside",
        description="Taken with Sony ILCE-6000",
        taken_at=datetime(2021, 1, 14),
        created_at=datetime(2021, 2, 8)
    )

    mc7 = Photo(
        user_id=4,
        photo='https://glimmr-photographs.s3.us-west-2.amazonaws.com/glimmrseederphotos/mc/mc7.jpg',
        title="Mountain Sunrise",
        description="taken with Sony ILCE-6000",
        taken_at=datetime(2020, 1, 5),
        created_at=datetime(2021, 1, 23)
    )

    mc8 = Photo(
        user_id=4,
        photo='https://glimmr-photographs.s3.us-west-2.amazonaws.com/glimmrseederphotos/mc/mc8.jpg',
        title="Italian Landscape",
        description="Taken with Sony ILCE-6000",
        taken_at=datetime(2020, 7, 25),
        created_at=datetime(2022, 5, 8)
    )

    mc9 = Photo(
        user_id=4,
        photo='https://glimmr-photographs.s3.us-west-2.amazonaws.com/glimmrseederphotos/mc/mc9.jpg',
        title="Art of Landscape",
        description="Dreamlike",
        taken_at=datetime(2023, 2, 9),
        created_at=datetime(2023, 3, 4)
    )

    mj1 = Photo(
        user_id=5,
        photo='https://glimmr-photographs.s3.us-west-2.amazonaws.com/glimmrseederphotos/mj/mj1.jpg',
        title="Neuschwanstein Castle",
        description="taken with Canon EOS 5D Mark II",
        taken_at=datetime(2020, 10, 13),
        created_at=datetime(2020, 10, 15)
    )

    mj2 = Photo(
        user_id=5,
        photo='https://glimmr-photographs.s3.us-west-2.amazonaws.com/glimmrseederphotos/mj/mj2.jpg',
        title="Vosges du Nord",
        description="Taken with Sony ILCE-7",
        taken_at=datetime(2020, 8, 4),
        created_at=datetime(2020, 4, 13)
    )

    mj3 = Photo(
        user_id=5,
        photo='https://glimmr-photographs.s3.us-west-2.amazonaws.com/glimmrseederphotos/mj/mj3.jpg',
        title="Höfats",
        description="Allgäu Alps",
        taken_at=datetime(2020, 6, 13),
        created_at=datetime(2020, 8, 31)
    )

    mj4 = Photo(
        user_id=5,
        photo='https://glimmr-photographs.s3.us-west-2.amazonaws.com/glimmrseederphotos/mj/mj4.jpg',
        title="Château du Hohenbourg",
        description="Taken with Canon EOS 7D",
        taken_at=datetime(2020, 9, 2),
        created_at=datetime(2020, 9, 14)
    )

    mj5 = Photo(
        user_id=5,
        photo='https://glimmr-photographs.s3.us-west-2.amazonaws.com/glimmrseederphotos/mj/mj5.jpg',
        title="Felsglühen",
        description="The Altschlossfelsen are a 1.5km long rock wall in the Palatinate Forest, not far away from the French border. They are known for the fact that in spring one of the rocks appear to glow in the light of the setting sun.",
        taken_at=datetime(2019, 4, 11),
        created_at=datetime(2019, 4, 15)
    )

    mj6 = Photo(
        user_id=5,
        photo='https://glimmr-photographs.s3.us-west-2.amazonaws.com/glimmrseederphotos/mj/mj6.jpg',
        title="Vosges du Nord",
        description="Taken with Sony ILCE-7",
        taken_at=datetime(2022, 1, 11),
        created_at=datetime(2023, 5, 19)
    )

    mj7 = Photo(
        user_id=5,
        photo='https://glimmr-photographs.s3.us-west-2.amazonaws.com/glimmrseederphotos/mj/mj7.jpg',
        title="Schlicker Seespitze seen from Hoher Burgstall",
        description="Sir Edmund Hillary chose the Hoher Burgstall as his first alpine peak during his 1949 trip to the Stubai Alps.",
        taken_at=datetime(2021, 8, 6),
        created_at=datetime(2023, 4, 24)
    )

    mj8 = Photo(
        user_id=5,
        photo='https://glimmr-photographs.s3.us-west-2.amazonaws.com/glimmrseederphotos/mj/mj8.jpg',
        title="Elfer, Stubai Alps",
        description="Today, April 22 is Earth Day",
        taken_at=datetime(2021, 8, 5),
        created_at=datetime(2023, 4, 22)
    )

    mj9 = Photo(
        user_id=5,
        photo='https://glimmr-photographs.s3.us-west-2.amazonaws.com/glimmrseederphotos/mj/mj9.jpg',
        title="View from Nebelhorn",
        description="Allgäu Alps",
        taken_at=datetime(2021, 7, 6),
        created_at=datetime(2023, 4, 19)
    )

    md1 = Photo(
        user_id=6,
        photo='https://glimmr-photographs.s3.us-west-2.amazonaws.com/glimmrseederphotos/md/md1.png',
        title="On The Edge Of A Volcano Crater",
        description="Haleakalā - meaning (house of the sun), or the East Maui Volcano, is a massive shield volcano that forms more than 75 percent of the Hawaiian Island of Maui. The crater measures 11.25 km (7 miles) in diameter.",
        taken_at=datetime(2021, 3, 20),
        created_at=datetime(2021, 3, 28)
    )

    md2 = Photo(
        user_id=6,
        photo='https://glimmr-photographs.s3.us-west-2.amazonaws.com/glimmrseederphotos/md/md2.jpg',
        title="The Twelve Apostles - Australia",
        description="The Twelve Apostles is a collection of limestone stacks off the shore of Port Campbell National Park, by the Great Ocean Road in Victoria, Australia. Their proximity to one another has made the site a popular tourist attraction.",
        taken_at=datetime(2020, 2, 22),
        created_at=datetime(2020, 6, 10)
    )


    md3 = Photo(
        user_id=6,
        photo='https://glimmr-photographs.s3.us-west-2.amazonaws.com/glimmrseederphotos/md/md3.png',
        title="Crystal Clear Cove - Sardinia, Italy",
        description="Later in the afternoon the suns angle gave an amazing oceanside underwater view of this beautiful paradise in Sardinia.",
        taken_at=datetime(2022, 6, 12),
        created_at=datetime(2022, 6, 29)
    )

    md4 = Photo(
        user_id=6,
        photo='https://glimmr-photographs.s3.us-west-2.amazonaws.com/glimmrseederphotos/md/md4.png',
        title="Whitehaven Beach - Australia",
        description=
        """
        One of the most beautiful beaches in Australia, Whitehaven is a sublime 7 kilometer slice of white silica sand and turquoise sea. Located at the northern end of Whitehaven Beach on Whitsunday Island, Hill Inlet Lookout is one of the jewels of the Australian landscape.

        No two visits to Hill Inlet are the same. As the tide flows, so does the sand, capturing swirling patterns in the turquoise waters. From the air, it looks like an abstract watercolour painting.
        """,
        taken_at=datetime(2022, 4, 6),
        created_at=datetime(2022, 4, 17)
    )

    md5 = Photo(
        user_id=6,
        photo='https://glimmr-photographs.s3.us-west-2.amazonaws.com/glimmrseederphotos/md/md5.jpg',
        title="Sainte-Lucie-de-Tallano - South of Corsica",
        description=
        """
        The village of Sainte-Lucie-de-Tallano is a small village located south east of France in Corsica. Located at 460m high in direction of the Gulf of Valincu, this village is surprising because of its architecture. It is composed of tall granite houses and narrow streets. The Roman Church Saint Jean Baptiste (XIIth century)
        - made of well cut stones, its immense door, its nave and the central axe make this chapel a work of art of Roman architecture.
        """,
        taken_at=datetime(2021, 9, 21),
        created_at=datetime(2021, 10, 9)
    )

    md6 = Photo(
        user_id=6,
        photo='https://glimmr-photographs.s3.us-west-2.amazonaws.com/glimmrseederphotos/md/md6.jpg',
        title="Ponto Vecchio At Sunset - Florence, Italy",
        description="Ponte Vecchio Bridge - is the most famous bridge in Florence and undoubtedly one of the city’s most illustrious landmarks. It is an incredibly breathtaking sight when seen from afar, and even more so when you walk across it!",
        taken_at=datetime(2014, 6, 3),
        created_at=datetime(2016, 12, 23)
    )

    md7 = Photo(
        user_id=6,
        photo='https://glimmr-photographs.s3.us-west-2.amazonaws.com/glimmrseederphotos/md/md7.png',
        title="Lazy Koala",
        description=
        """
        Formerly killed in huge numbers for their fur, especially during the 1920s and ’30s, koalas dwindled in number from several million to a few hundred thousand. In the southern part of their range, they became practically extinct except for a single population in Gippsland, Victoria in Australia. Some were translocated onto small offshore islands, especially Phillip Island, where they did so well that these koalas were used to restock much of the original range in Victoria and southern New South Wales, Australia.
        """,
        taken_at=datetime(2020, 4, 19),
        created_at=datetime(2020, 4, 28)
    )


    md8 = Photo(
        user_id=6,
        photo='https://glimmr-photographs.s3.us-west-2.amazonaws.com/glimmrseederphotos/md/md8.jpg',
        title="Moon Orchids",
        description="(Phalaenopsis amabilis) Moon Orchid lives by sticking to stems or other plants in forests and can grow at an elevation of 600 meters above sea level. Moon Orchid can easily be found in Southeast Asia such as Indonesia, Malaysia, the Philippines, and also in Australia.",
        taken_at=datetime(2020, 10, 27),
        created_at=datetime(2023, 11, 1)
    )

    md9 = Photo(
        user_id=6,
        photo='https://glimmr-photographs.s3.us-west-2.amazonaws.com/glimmrseederphotos/md/md9.png',
        title="Ausable River - New York",
        description='The Ausable River, also known as AuSable River and originally written as "Au Sable", runs in the U.S. state of New York, from the Adirondack Mountains and past the village of Lake Placid and Au Sable Forks to empty into Lake Champlain.',
        taken_at=datetime(2022, 6, 6),
        created_at=datetime(2022, 9, 5)
    )

    md10 = Photo(
        user_id=6,
        photo='https://glimmr-photographs.s3.us-west-2.amazonaws.com/glimmrseederphotos/md/md10.jpg',
        title="Horseshoe Bay, Bowen, Queensland, Australia",
        description="If you are travelling along Australia’s east coast, be sure to plan a stop in the coastal town of Bowen. North Queensland’s oldest town, Bowen is well known for two main reasons - it is the home of Bowen Mangoes (a popular variety of the mango fruit) and it was the main filming location for the famous movie Australia in 2008. Bowen is one of the only places on Australia’s east coast that you can walk straight of the shore into the water and explore the reef.",
        taken_at=datetime(2020, 3, 6),
        created_at=datetime(2020, 12, 16)
    )

    sm1 = Photo(
        user_id=7,
        photo='https://glimmr-photographs.s3.us-west-2.amazonaws.com/glimmrseederphotos/sm/sm1.jpg',
        title="Winter River of Gold - River Shiel, Blain, Moidart",
        description="The old bridge over the River Shiel at dawn after a fresh fall of overnight snow, with the golden light of the rising sun colouring the mist in the sky and the surface of the river as well.",
        taken_at=datetime(2021, 1, 23),
        created_at=datetime(2022, 8, 6)
    )

    sm2 = Photo(
        user_id=7,
        photo='https://glimmr-photographs.s3.us-west-2.amazonaws.com/glimmrseederphotos/sm/sm2.jpg',
        title="Castle Tioram from Kinlochmoidart, Moidart",
        description="Castle Tioram viewed from across Loch Moidart looking south-west through the gap in between Eilean an Fheidh and Eilean Shona as the golden hazy light of a setting winter sun separates it from the hills of Ardnamurchan beyond.",
        taken_at=datetime(2021, 1, 11),
        created_at=datetime(2023, 1, 20)
    )

    sm3 = Photo(
        user_id=7,
        photo='https://glimmr-photographs.s3.us-west-2.amazonaws.com/glimmrseederphotos/sm/sm3.jpg',
        title="Day's End, Land's End - Ardnamurchan Lighthouse",
        description="A midsummer day comes to an end as the sun dips below the north-western horizon, out beyond the tower of Ardnamurchan Lighthouse",
        taken_at=datetime(2022, 7, 19),
        created_at=datetime(2023, 7, 19)
    )

    sm4 = Photo(
        user_id=7,
        photo='https://glimmr-photographs.s3.us-west-2.amazonaws.com/glimmrseederphotos/sm/sm4.jpg',
        title="Inbhir Allt na Luachair, Portuairk, Ardnamurchan",
        description="The rugged peaks of the Rùm Cuillin silhouetted against the orange of a dusk sky, viewed immediately after sunset from amongst the rocky shoreline of Inbhir Allt na Luachair",
        taken_at=datetime(2022, 3, 30),
        created_at=datetime(2023, 3, 4)
    )

    sm5 = Photo(
        user_id=7,
        photo='https://glimmr-photographs.s3.us-west-2.amazonaws.com/glimmrseederphotos/sm/sm5.jpg',
        title="Kentra Bay, Arivegaig, Ardnamurchan",
        description="On the morning of 30 December 2020, a Cold Full Moon and the last full moon of the year and of the decade travels over the Small Isles of Eigg and Rum, out beyond the entrance of Kentra Bay, about an hour or so before it would set in the north-west.",
        taken_at=datetime(2020, 12, 30),
        created_at=datetime(2022, 12, 12)
    )

    sm6 = Photo(
        user_id=7,
        photo='https://glimmr-photographs.s3.us-west-2.amazonaws.com/glimmrseederphotos/sm/sm6.jpg',
        title="River Shiel, Blain, Moidart",
        description="As a day in early November comes to a close, the setting autumn sun breaks through the trees, lighting up the parapet of the old bridge over the River Shiel and the trees along the riverbank.",
        taken_at=datetime(2021, 11, 25),
        created_at=datetime(2022, 11, 3)
    )

    sm7 = Photo(
        user_id=7,
        photo='https://glimmr-photographs.s3.us-west-2.amazonaws.com/glimmrseederphotos/sm/sm7.jpg',
        title="Loch Sunart, Resipole, Sunart",
        description="A silvery Loch Sunart shimmering under the grey and overcast sky of a January morning",
        taken_at=datetime(2022, 1, 20),
        created_at=datetime(2023, 2, 10)
    )

    sm8 = Photo(
        user_id=7,
        photo='https://glimmr-photographs.s3.us-west-2.amazonaws.com/glimmrseederphotos/sm/sm8.jpg',
        title="Lochan Doire a' Bhraghaid, Inversanda, Ardgour",
        description="A cold January morning with a waning crescent moon sitting above Lochan Doire a' Bhraghaid and the orange of a rising sun colouring its frozen surface and the sky above the hills beyond.",
        taken_at=datetime(2021, 1, 8),
        created_at=datetime(2023, 1, 27)
    )

    sm9 = Photo(
        user_id=7,
        photo='https://glimmr-photographs.s3.us-west-2.amazonaws.com/glimmrseederphotos/sm/sm9.jpg',
        title="Sailean nan Cuileag, Salen, Ardnamurchan",
        description="The last of the ice from the prolonged cold spell of early 2021 clings on to the fringes of Sailean nan Cuileag as it loses the battle against a rising tide during sunset on a calm winter evening.",
        taken_at=datetime(2021, 2, 9),
        created_at=datetime(2023, 2, 14)
    )

    sm10 = Photo(
        user_id=7,
        photo='https://glimmr-photographs.s3.us-west-2.amazonaws.com/glimmrseederphotos/sm/sm10.jpg',
        title="Loch Sunart, Glenborrodale, Ardnamurchan",
        description="The first light of a spring day falling on the island of Risga and the skerries around it, while the isle of Carna sits in the morning haze in the background.",
        taken_at=datetime(2022, 4, 19),
        created_at=datetime(2022, 5, 22)
    )

    pm1 = Photo(
        user_id=8,
        photo='https://glimmr-photographs.s3.us-west-2.amazonaws.com/glimmrseederphotos/pm/pm1.jpg',
        title="Tree",
        description="Thank you for taking the time to view my photo, maybe for your faves and comments, I appreciate that very much!",
        taken_at=datetime(2021, 1, 8),
        created_at=datetime(2021, 1, 11)
    )

    pm2 = Photo(
        user_id=8,
        photo='https://glimmr-photographs.s3.us-west-2.amazonaws.com/glimmrseederphotos/pm/pm2.jpg',
        title="A View from My Window",
        description="Thanks for your visit, faves and comments, I appreciate that very much!",
        taken_at=datetime(2018, 11, 6),
        created_at=datetime(2018, 11, 9)
    )

    pm3 = Photo(
        user_id=8,
        photo='https://glimmr-photographs.s3.us-west-2.amazonaws.com/glimmrseederphotos/pm/pm3.jpg',
        title="Blue Hour",
        description="Thank you for taking the time to view my photo, maybe for your faves and comments, I appreciate that very much!",
        taken_at=datetime(2021, 2, 21),
        created_at=datetime(2021, 2, 26)
    )

    pm4 = Photo(
        user_id=8,
        photo='https://glimmr-photographs.s3.us-west-2.amazonaws.com/glimmrseederphotos/pm/pm4.jpg',
        title="The Guardians",
        description="Thank you for taking the time to view my photo, maybe for your faves and comments, I appreciate that very much!",
        taken_at=datetime(2021, 11, 9),
        created_at=datetime(2022, 1, 10)
    )

    pm5 = Photo(
        user_id=8,
        photo='https://glimmr-photographs.s3.us-west-2.amazonaws.com/glimmrseederphotos/pm/pm5.jpg',
        title="Madeira",
        description="Real sun, no Luminar",
        taken_at=datetime(2021, 11, 7),
        created_at=datetime(2021, 11, 17)
    )

    pm6 = Photo(
        user_id=8,
        photo='https://glimmr-photographs.s3.us-west-2.amazonaws.com/glimmrseederphotos/pm/pm6.jpg',
        title="Sunset",
        description="Thank you for taking the time to view my photo, maybe for your faves and comments, I appreciate that very much!",
        taken_at=datetime(2023, 5, 17),
        created_at=datetime(2023, 6, 12)
    )

    pm7 = Photo(
        user_id=8,
        photo='https://glimmr-photographs.s3.us-west-2.amazonaws.com/glimmrseederphotos/pm/pm7.jpg',
        title="Bláhylur",
        description="Panorama made from 4 shots",
        taken_at=datetime(2022, 7, 10),
        created_at=datetime(2022, 7, 18)
    )

    pm8 = Photo(
        user_id=8,
        photo='https://glimmr-photographs.s3.us-west-2.amazonaws.com/glimmrseederphotos/pm/pm8.jpg',
        title="Kerlingarfjöll",
        description="Thank you for taking the time to view my photo, maybe for your faves and comments, I appreciate that very much!",
        taken_at=datetime(2022, 7, 8),
        created_at=datetime(2023, 7, 20)
    )

    pm9 = Photo(
        user_id=8,
        photo='https://glimmr-photographs.s3.us-west-2.amazonaws.com/glimmrseederphotos/pm/pm9.jpg',
        title="Autumn",
        description="Thank you for taking the time to view my photo, maybe for your faves and comments, I appreciate that very much!",
        taken_at=datetime(2022, 10, 28),
        created_at=datetime(2022, 11, 4)
    )

    pm10 = Photo(
        user_id=8,
        photo='https://glimmr-photographs.s3.us-west-2.amazonaws.com/glimmrseederphotos/pm/pm10.jpg',
        title="Goðafoss",
        description="Thank you for taking the time to view my photo, maybe for your faves and comments, I appreciate that very much!",
        taken_at=datetime(2022, 9, 7),
        created_at=datetime(2022, 7, 5)
    )

    all_photos = [
                demo1, demo2, demo3, demo4, demo5, demo6, demo7, demo8, demo9, demo10, demo11,
                dp1, dp2, dp3, dp4, dp5, dp6, dp7, dp8, dp9, dp10, dp11, dp12, dp13, dp14, dp15,
                jy1, jy2, jy3, jy4, jy5, jy6, jy7, jy8, jy9, jy10, jy11,
                mc1, mc2, mc3, mc4, mc5, mc6, mc7, mc8, mc9,
                mj1, mj2, mj3, mj4, mj5, mj6, mj7, mj8, mj9,
                md1, md2, md3, md4, md5, md6, md7, md8, md9, md10,
                sm1, sm2, sm3, sm4, sm5, sm6, sm7, sm8, sm9, sm10,
                pm1, pm2, pm3, pm4, pm5, pm6, pm7, pm8, pm9, pm10
                ]

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
