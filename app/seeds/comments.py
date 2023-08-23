from app.models import db, Comment, environment, SCHEMA
from sqlalchemy.sql import text
from datetime import datetime

positive_comments = [
    "Great composition!",
    "Beautiful colors!",
    "Amazing shot!",
    "Well captured!",
    "Stunning view!",
    "Lovely photo!",
    "Impressive!",
    "Fantastic shot!",
    "Brilliant colors!",
    "Incredible!",
    "Well done!",
    "Absolutely stunning",
    "Pure perfection",
    "Fantastic!",
    "Such a beautiful capture",
    "I'm amazed!",
    "Outstanding work",
    "Wonderful shot",
    "This is incredible",
    "A masterpiece",
    "Absolutely gorgeous",
    "So lovely",
    "Wonderful colors",
    "Breathtaking",
    "Lovely composition",
    "Speechless",
    "Captivating",
    "Great shot!",
    "Such beauty",
    "Wow!",
]

def seed_comments():
    comment1 = Comment(user_id=9, photo_id=1, text='Stunning view!', created_at=datetime(2023, 7, 12), updated_at=datetime(2023, 7, 12))
    comment2 = Comment(user_id=3, photo_id=2, text='Fantastic shot!', created_at=datetime(2023, 7, 12), updated_at=datetime(2023, 7, 12))
    comment3 = Comment(user_id=9, photo_id=2, text='Beautiful colors!', created_at=datetime(2023, 7, 13), updated_at=datetime(2023, 7, 13))
    comment4 = Comment(user_id=6, photo_id=2, text='Amazing shot!', created_at=datetime(2023, 7, 14), updated_at=datetime(2023, 7, 14))
    comment5 = Comment(user_id=2, photo_id=3, text='Lovely composition', created_at=datetime(2023, 7, 12), updated_at=datetime(2023, 7, 12))
    comment6 = Comment(user_id=6, photo_id=3, text='Such beauty', created_at=datetime(2023, 7, 13), updated_at=datetime(2023, 7, 13))
    comment7 = Comment(user_id=2, photo_id=4, text='Great composition!', created_at=datetime(2023, 7, 12), updated_at=datetime(2023, 7, 12))
    comment8 = Comment(user_id=3, photo_id=4, text='Amazing shot!', created_at=datetime(2023, 7, 13), updated_at=datetime(2023, 7, 13))
    comment9 = Comment(user_id=8, photo_id=4, text='Stunning view!', created_at=datetime(2023, 7, 14), updated_at=datetime(2023, 7, 14))
    comment10 = Comment(user_id=6, photo_id=4, text='Lovely composition', created_at=datetime(2023, 7, 15), updated_at=datetime(2023, 7, 15))
    comment11 = Comment(user_id=4, photo_id=5, text='Well done!', created_at=datetime(2023, 7, 12), updated_at=datetime(2023, 7, 12))
    comment12 = Comment(user_id=3, photo_id=5, text='Fantastic shot!', created_at=datetime(2023, 7, 13), updated_at=datetime(2023, 7, 13))
    comment13 = Comment(user_id=10, photo_id=6, text='I\'m amazed!', created_at=datetime(2023, 7, 12), updated_at=datetime(2023, 7, 12))
    comment14 = Comment(user_id=5, photo_id=6, text='Outstanding work', created_at=datetime(2023, 7, 13), updated_at=datetime(2023, 7, 13))
    comment15 = Comment(user_id=5, photo_id=7, text='Fantastic!', created_at=datetime(2023, 7, 12), updated_at=datetime(2023, 7, 12))
    comment16 = Comment(user_id=3, photo_id=7, text='Such a beautiful capture', created_at=datetime(2023, 7, 13), updated_at=datetime(2023, 7, 13))
    comment17 = Comment(user_id=8, photo_id=7, text='Lovely photo!', created_at=datetime(2023, 7, 14), updated_at=datetime(2023, 7, 14))
    comment18 = Comment(user_id=2, photo_id=8, text='Brilliant colors!', created_at=datetime(2023, 7, 12), updated_at=datetime(2023, 7, 12))
    comment19 = Comment(user_id=9, photo_id=8, text='Well captured!', created_at=datetime(2023, 7, 13), updated_at=datetime(2023, 7, 13))
    comment20 = Comment(user_id=8, photo_id=9, text='Stunning view!', created_at=datetime(2023, 7, 12), updated_at=datetime(2023, 7, 12))
    comment21 = Comment(user_id=10, photo_id=9, text='Lovely photo!', created_at=datetime(2023, 7, 13), updated_at=datetime(2023, 7, 13))
    comment22 = Comment(user_id=6, photo_id=9, text='Impressive!', created_at=datetime(2023, 7, 14), updated_at=datetime(2023, 7, 14))
    comment23 = Comment(user_id=4, photo_id=10, text='Great shot!', created_at=datetime(2023, 7, 12), updated_at=datetime(2023, 7, 12))
    comment24 = Comment(user_id=3, photo_id=10, text='Fantastic shot!', created_at=datetime(2023, 7, 13), updated_at=datetime(2023, 7, 13))
    comment25 = Comment(user_id=7, photo_id=11, text='Lovely composition', created_at=datetime(2023, 7, 12), updated_at=datetime(2023, 7, 12))
    comment26 = Comment(user_id=8, photo_id=11, text='Stunning view!', created_at=datetime(2023, 7, 13), updated_at=datetime(2023, 7, 13))
    comment27 = Comment(user_id=3, photo_id=11, text='Amazing shot!', created_at=datetime(2023, 7, 14), updated_at=datetime(2023, 7, 14))
    comment28 = Comment(user_id=5, photo_id=12, text='Fantastic!', created_at=datetime(2023, 7, 12), updated_at=datetime(2023, 7, 12))
    comment29 = Comment(user_id=9, photo_id=12, text='Lovely photo!', created_at=datetime(2023, 7, 13), updated_at=datetime(2023, 7, 13))
    comment30 = Comment(user_id=1, photo_id=13, text='Great composition!', created_at=datetime(2023, 7, 12), updated_at=datetime(2023, 7, 12))
    comment31 = Comment(user_id=7, photo_id=13, text='Impressive!', created_at=datetime(2023, 7, 13), updated_at=datetime(2023, 7, 13))
    comment32 = Comment(user_id=4, photo_id=14, text='Well done!', created_at=datetime(2023, 7, 12), updated_at=datetime(2023, 7, 12))
    comment33 = Comment(user_id=10, photo_id=14, text='Outstanding work', created_at=datetime(2023, 7, 13), updated_at=datetime(2023, 7, 13))
    comment34 = Comment(user_id=5, photo_id=14, text='Amazing shot!', created_at=datetime(2023, 7, 14), updated_at=datetime(2023, 7, 14))
    comment35 = Comment(user_id=7, photo_id=15, text='Lovely composition', created_at=datetime(2023, 7, 12), updated_at=datetime(2023, 7, 12))
    comment36 = Comment(user_id=4, photo_id=16, text='Lovely composition', created_at=datetime(2023, 7, 12), updated_at=datetime(2023, 7, 12))
    comment37 = Comment(user_id=8, photo_id=16, text='Fantastic!', created_at=datetime(2023, 7, 13), updated_at=datetime(2023, 7, 13))
    comment38 = Comment(user_id=9, photo_id=16, text='Beautiful colors!', created_at=datetime(2023, 7, 14), updated_at=datetime(2023, 7, 14))
    comment39 = Comment(user_id=3, photo_id=16, text='Well done!', created_at=datetime(2023, 7, 15), updated_at=datetime(2023, 7, 15))
    comment40 = Comment(user_id=6, photo_id=17, text='Great shot!', created_at=datetime(2023, 7, 12), updated_at=datetime(2023, 7, 12))
    comment41 = Comment(user_id=5, photo_id=17, text='Stunning view!', created_at=datetime(2023, 7, 13), updated_at=datetime(2023, 7, 13))
    comment42 = Comment(user_id=4, photo_id=17, text='Fantastic shot!', created_at=datetime(2023, 7, 14), updated_at=datetime(2023, 7, 14))
    comment43 = Comment(user_id=8, photo_id=18, text='Great composition!', created_at=datetime(2023, 7, 12), updated_at=datetime(2023, 7, 12))
    comment44 = Comment(user_id=9, photo_id=18, text='Beautiful colors!', created_at=datetime(2023, 7, 13), updated_at=datetime(2023, 7, 13))
    comment45 = Comment(user_id=7, photo_id=18, text='Impressive!', created_at=datetime(2023, 7, 14), updated_at=datetime(2023, 7, 14))
    comment46 = Comment(user_id=6, photo_id=18, text='Fantastic shot!', created_at=datetime(2023, 7, 15), updated_at=datetime(2023, 7, 15))
    comment47 = Comment(user_id=3, photo_id=19, text='Stunning view!', created_at=datetime(2023, 7, 12), updated_at=datetime(2023, 7, 12))
    comment48 = Comment(user_id=5, photo_id=19, text='Lovely photo!', created_at=datetime(2023, 7, 13), updated_at=datetime(2023, 7, 13))
    comment49 = Comment(user_id=10, photo_id=19, text='Fantastic!', created_at=datetime(2023, 7, 14), updated_at=datetime(2023, 7, 14))
    comment50 = Comment(user_id=4, photo_id=20, text='Well done!', created_at=datetime(2023, 7, 12), updated_at=datetime(2023, 7, 12))

    comment51 = Comment(user_id=8, photo_id=20, text='Great composition!', created_at=datetime(2023, 7, 13), updated_at=datetime(2023, 7, 13))
    comment52 = Comment(user_id=5, photo_id=20, text='Beautiful colors!', created_at=datetime(2023, 7, 14), updated_at=datetime(2023, 7, 14))
    comment53 = Comment(user_id=3, photo_id=20, text='Amazing shot!', created_at=datetime(2023, 7, 15), updated_at=datetime(2023, 7, 15))
    comment54 = Comment(user_id=6, photo_id=21, text='Well captured!', created_at=datetime(2023, 7, 12), updated_at=datetime(2023, 7, 12))
    comment55 = Comment(user_id=8, photo_id=21, text='Stunning view!', created_at=datetime(2023, 7, 13), updated_at=datetime(2023, 7, 13))
    comment56 = Comment(user_id=1, photo_id=21, text='Lovely photo!', created_at=datetime(2023, 7, 14), updated_at=datetime(2023, 7, 14))
    comment57 = Comment(user_id=7, photo_id=22, text='Impressive!', created_at=datetime(2023, 7, 12), updated_at=datetime(2023, 7, 12))
    comment58 = Comment(user_id=5, photo_id=22, text='Fantastic shot!', created_at=datetime(2023, 7, 13), updated_at=datetime(2023, 7, 13))
    comment59 = Comment(user_id=4, photo_id=22, text='Brilliant colors!', created_at=datetime(2023, 7, 14), updated_at=datetime(2023, 7, 14))
    comment60 = Comment(user_id=3, photo_id=22, text='Incredible!', created_at=datetime(2023, 7, 15), updated_at=datetime(2023, 7, 15))
    comment61 = Comment(user_id=10, photo_id=23, text='Well done!', created_at=datetime(2023, 7, 12), updated_at=datetime(2023, 7, 12))
    comment62 = Comment(user_id=9, photo_id=23, text='Absolutely stunning', created_at=datetime(2023, 7, 13), updated_at=datetime(2023, 7, 13))
    comment63 = Comment(user_id=10, photo_id=24, text='Pure perfection', created_at=datetime(2023, 7, 12), updated_at=datetime(2023, 7, 12))
    comment64 = Comment(user_id=3, photo_id=24, text='Fantastic!', created_at=datetime(2023, 7, 13), updated_at=datetime(2023, 7, 13))
    comment65 = Comment(user_id=1, photo_id=24, text='Such a beautiful capture', created_at=datetime(2023, 7, 14), updated_at=datetime(2023, 7, 14))
    comment66 = Comment(user_id=5, photo_id=25, text="I'm amazed!", created_at=datetime(2023, 7, 12), updated_at=datetime(2023, 7, 12))
    comment67 = Comment(user_id=3, photo_id=25, text='Outstanding work', created_at=datetime(2023, 7, 13), updated_at=datetime(2023, 7, 13))
    comment68 = Comment(user_id=8, photo_id=25, text='Wonderful shot', created_at=datetime(2023, 7, 14), updated_at=datetime(2023, 7, 14))
    comment69 = Comment(user_id=9, photo_id=26, text='This is incredible', created_at=datetime(2023, 7, 12), updated_at=datetime(2023, 7, 12))
    comment70 = Comment(user_id=7, photo_id=26, text='A masterpiece', created_at=datetime(2023, 7, 13), updated_at=datetime(2023, 7, 13))
    comment71 = Comment(user_id=10, photo_id=26, text='Absolutely gorgeous', created_at=datetime(2023, 7, 14), updated_at=datetime(2023, 7, 14))
    comment72 = Comment(user_id=2, photo_id=27, text='So lovely', created_at=datetime(2023, 7, 12), updated_at=datetime(2023, 7, 12))
    comment73 = Comment(user_id=4, photo_id=27, text='Wonderful colors', created_at=datetime(2023, 7, 13), updated_at=datetime(2023, 7, 13))
    comment74 = Comment(user_id=6, photo_id=27, text='Breathtaking', created_at=datetime(2023, 7, 14), updated_at=datetime(2023, 7, 14))
    comment75 = Comment(user_id=9, photo_id=27, text='Lovely composition', created_at=datetime(2023, 7, 15), updated_at=datetime(2023, 7, 15))
    comment76 = Comment(user_id=5, photo_id=28, text='Speechless', created_at=datetime(2023, 7, 12), updated_at=datetime(2023, 7, 12))
    comment77 = Comment(user_id=4, photo_id=28, text='Captivating', created_at=datetime(2023, 7, 13), updated_at=datetime(2023, 7, 13))
    comment78 = Comment(user_id=7, photo_id=28, text='Great shot!', created_at=datetime(2023, 7, 14), updated_at=datetime(2023, 7, 14))
    comment79 = Comment(user_id=6, photo_id=28, text='Such beauty', created_at=datetime(2023, 7, 15), updated_at=datetime(2023, 7, 15))
    comment80 = Comment(user_id=1, photo_id=29, text='Wow!', created_at=datetime(2023, 7, 12), updated_at=datetime(2023, 7, 12))
    comment81 = Comment(user_id=5, photo_id=30, text='Great composition!', created_at=datetime(2023, 7, 12), updated_at=datetime(2023, 7, 12))
    comment82 = Comment(user_id=6, photo_id=30, text='Beautiful colors!', created_at=datetime(2023, 7, 13), updated_at=datetime(2023, 7, 13))
    comment83 = Comment(user_id=9, photo_id=30, text='Amazing shot!', created_at=datetime(2023, 7, 14), updated_at=datetime(2023, 7, 14))
    comment84 = Comment(user_id=2, photo_id=31, text='Well captured!', created_at=datetime(2023, 7, 12), updated_at=datetime(2023, 7, 12))
    comment85 = Comment(user_id=4, photo_id=31, text='Stunning view!', created_at=datetime(2023, 7, 13), updated_at=datetime(2023, 7, 13))
    comment86 = Comment(user_id=7, photo_id=32, text='Lovely photo!', created_at=datetime(2023, 7, 12), updated_at=datetime(2023, 7, 12))
    comment87 = Comment(user_id=2, photo_id=32, text='Impressive!', created_at=datetime(2023, 7, 13), updated_at=datetime(2023, 7, 13))
    comment88 = Comment(user_id=4, photo_id=33, text='Fantastic shot!', created_at=datetime(2023, 7, 12), updated_at=datetime(2023, 7, 12))
    comment89 = Comment(user_id=7, photo_id=33, text='Brilliant colors!', created_at=datetime(2023, 7, 13), updated_at=datetime(2023, 7, 13))
    comment90 = Comment(user_id=1, photo_id=34, text='Incredible!', created_at=datetime(2023, 7, 12), updated_at=datetime(2023, 7, 12))
    comment91 = Comment(user_id=6, photo_id=35, text='Well done!', created_at=datetime(2023, 7, 12), updated_at=datetime(2023, 7, 12))
    comment92 = Comment(user_id=7, photo_id=36, text='Absolutely stunning', created_at=datetime(2023, 7, 12), updated_at=datetime(2023, 7, 12))
    comment93 = Comment(user_id=9, photo_id=37, text='Pure perfection', created_at=datetime(2023, 7, 12), updated_at=datetime(2023, 7, 12))
    comment94 = Comment(user_id=2, photo_id=37, text='Fantastic!', created_at=datetime(2023, 7, 13), updated_at=datetime(2023, 7, 13))
    comment95 = Comment(user_id=8, photo_id=37, text='Such a beautiful capture', created_at=datetime(2023, 7, 14), updated_at=datetime(2023, 7, 14))
    comment96 = Comment(user_id=7, photo_id=38, text="I'm amazed!", created_at=datetime(2023, 7, 12), updated_at=datetime(2023, 7, 12))
    comment97 = Comment(user_id=2, photo_id=38, text='Outstanding work', created_at=datetime(2023, 7, 13), updated_at=datetime(2023, 7, 13))
    comment98 = Comment(user_id=2, photo_id=39, text='Wonderful colors', created_at=datetime(2023, 7, 12), updated_at=datetime(2023, 7, 12))
    comment99 = Comment(user_id=5, photo_id=39, text='Breathtaking', created_at=datetime(2023, 7, 13), updated_at=datetime(2023, 7, 13))
    comment100 = Comment(user_id=6, photo_id=40, text='Lovely composition', created_at=datetime(2023, 7, 12), updated_at=datetime(2023, 7, 12))

    comment101 = Comment(user_id=5, photo_id=41, text='Nice shot!', created_at=datetime(2023, 7, 12), updated_at=datetime(2023, 7, 12))
    comment102 = Comment(user_id=7, photo_id=42, text='Great composition', created_at=datetime(2023, 7, 12), updated_at=datetime(2023, 7, 12))
    comment103 = Comment(user_id=5, photo_id=43, text='Beautiful colors', created_at=datetime(2023, 7, 12), updated_at=datetime(2023, 7, 12))
    comment104 = Comment(user_id=6, photo_id=43, text='Fantastic shot!', created_at=datetime(2023, 7, 12), updated_at=datetime(2023, 7, 12))
    comment105 = Comment(user_id=7, photo_id=43, text='Impressive', created_at=datetime(2023, 7, 12), updated_at=datetime(2023, 7, 12))
    comment106 = Comment(user_id=8, photo_id=44, text='Well done!', created_at=datetime(2023, 7, 12), updated_at=datetime(2023, 7, 12))
    comment107 = Comment(user_id=9, photo_id=44, text='Stunning view', created_at=datetime(2023, 7, 12), updated_at=datetime(2023, 7, 12))
    comment108 = Comment(user_id=10, photo_id=44, text='Lovely photo', created_at=datetime(2023, 7, 12), updated_at=datetime(2023, 7, 12))
    comment109 = Comment(user_id=1, photo_id=45, text='Impressive shot', created_at=datetime(2023, 7, 12), updated_at=datetime(2023, 7, 12))
    comment110 = Comment(user_id=5, photo_id=45, text='Fantastic work', created_at=datetime(2023, 7, 12), updated_at=datetime(2023, 7, 12))
    comment111 = Comment(user_id=1, photo_id=46, text='Wow!', created_at=datetime(2023, 7, 12), updated_at=datetime(2023, 7, 12))
    comment112 = Comment(user_id=2, photo_id=46, text='Brilliant colors', created_at=datetime(2023, 7, 12), updated_at=datetime(2023, 7, 12))
    comment113 = Comment(user_id=5, photo_id=46, text='Incredible shot', created_at=datetime(2023, 7, 12), updated_at=datetime(2023, 7, 12))
    comment114 = Comment(user_id=8, photo_id=47, text='Absolutely stunning', created_at=datetime(2023, 7, 12), updated_at=datetime(2023, 7, 12))
    comment115 = Comment(user_id=9, photo_id=47, text='Beautiful capture', created_at=datetime(2023, 7, 12), updated_at=datetime(2023, 7, 12))
    comment116 = Comment(user_id=10, photo_id=47, text='Fantastic job', created_at=datetime(2023, 7, 12), updated_at=datetime(2023, 7, 12))
    comment117 = Comment(user_id=1, photo_id=47, text='Impressive work', created_at=datetime(2023, 7, 12), updated_at=datetime(2023, 7, 12))
    comment118 = Comment(user_id=4, photo_id=48, text='Wonderful composition', created_at=datetime(2023, 7, 12), updated_at=datetime(2023, 7, 12))
    comment119 = Comment(user_id=2, photo_id=48, text='Beautiful shot', created_at=datetime(2023, 7, 12), updated_at=datetime(2023, 7, 12))
    comment120 = Comment(user_id=6, photo_id=48, text='Captivating', created_at=datetime(2023, 7, 12), updated_at=datetime(2023, 7, 12))
    comment121 = Comment(user_id=7, photo_id=48, text='Breathtaking', created_at=datetime(2023, 7, 12), updated_at=datetime(2023, 7, 12))
    comment122 = Comment(user_id=1, photo_id=49, text='Wow!', created_at=datetime(2023, 7, 12), updated_at=datetime(2023, 7, 12))
    comment123 = Comment(user_id=4, photo_id=49, text='Outstanding work', created_at=datetime(2023, 7, 12), updated_at=datetime(2023, 7, 12))
    comment124 = Comment(user_id=9, photo_id=49, text='Incredible shot', created_at=datetime(2023, 7, 12), updated_at=datetime(2023, 7, 12))
    comment125 = Comment(user_id=2, photo_id=50, text='Lovely composition', created_at=datetime(2023, 7, 12), updated_at=datetime(2023, 7, 12))
    comment126 = Comment(user_id=2, photo_id=51, text='Nice shot!', created_at=datetime(2023, 7, 12), updated_at=datetime(2023, 7, 12))
    comment127 = Comment(user_id=7, photo_id=51, text='Great composition', created_at=datetime(2023, 7, 12), updated_at=datetime(2023, 7, 12))
    comment128 = Comment(user_id=4, photo_id=52, text='Beautiful colors', created_at=datetime(2023, 7, 12), updated_at=datetime(2023, 7, 12))
    comment129 = Comment(user_id=9, photo_id=52, text='Fantastic shot!', created_at=datetime(2023, 7, 12), updated_at=datetime(2023, 7, 12))
    comment130 = Comment(user_id=6, photo_id=52, text='Impressive', created_at=datetime(2023, 7, 12), updated_at=datetime(2023, 7, 12))
    comment131 = Comment(user_id=7, photo_id=53, text='Well done!', created_at=datetime(2023, 7, 12), updated_at=datetime(2023, 7, 12))
    comment132 = Comment(user_id=8, photo_id=53, text='Stunning view', created_at=datetime(2023, 7, 12), updated_at=datetime(2023, 7, 12))
    comment133 = Comment(user_id=9, photo_id=53, text='Lovely photo', created_at=datetime(2023, 7, 12), updated_at=datetime(2023, 7, 12))
    comment134 = Comment(user_id=10, photo_id=53, text='Impressive shot', created_at=datetime(2023, 7, 12), updated_at=datetime(2023, 7, 12))
    comment135 = Comment(user_id=1, photo_id=54, text='Wow!', created_at=datetime(2023, 7, 12), updated_at=datetime(2023, 7, 12))
    comment136 = Comment(user_id=4, photo_id=54, text='Brilliant colors', created_at=datetime(2023, 7, 12), updated_at=datetime(2023, 7, 12))
    comment137 = Comment(user_id=9, photo_id=54, text='Incredible shot', created_at=datetime(2023, 7, 12), updated_at=datetime(2023, 7, 12))
    comment138 = Comment(user_id=6, photo_id=54, text='Absolutely stunning', created_at=datetime(2023, 7, 12), updated_at=datetime(2023, 7, 12))
    comment139 = Comment(user_id=7, photo_id=55, text='Beautiful capture', created_at=datetime(2023, 7, 12), updated_at=datetime(2023, 7, 12))
    comment140 = Comment(user_id=8, photo_id=55, text='Fantastic job', created_at=datetime(2023, 7, 12), updated_at=datetime(2023, 7, 12))
    comment141 = Comment(user_id=4, photo_id=56, text='Wonderful composition', created_at=datetime(2023, 7, 12), updated_at=datetime(2023, 7, 12))
    comment142 = Comment(user_id=5, photo_id=56, text='Beautiful shot', created_at=datetime(2023, 7, 12), updated_at=datetime(2023, 7, 12))
    comment143 = Comment(user_id=2, photo_id=56, text='Captivating', created_at=datetime(2023, 7, 12), updated_at=datetime(2023, 7, 12))
    comment144 = Comment(user_id=7, photo_id=57, text='Breathtaking', created_at=datetime(2023, 7, 12), updated_at=datetime(2023, 7, 12))
    comment145 = Comment(user_id=8, photo_id=57, text='Wow!', created_at=datetime(2023, 7, 12), updated_at=datetime(2023, 7, 12))
    comment146 = Comment(user_id=9, photo_id=57, text='Outstanding work', created_at=datetime(2023, 7, 12), updated_at=datetime(2023, 7, 12))
    comment147 = Comment(user_id=10, photo_id=57, text='Incredible shot', created_at=datetime(2023, 7, 12), updated_at=datetime(2023, 7, 12))
    comment148 = Comment(user_id=1, photo_id=58, text='Lovely composition', created_at=datetime(2023, 7, 12), updated_at=datetime(2023, 7, 12))
    comment149 = Comment(user_id=4, photo_id=59, text='Nice shot!', created_at=datetime(2023, 7, 12), updated_at=datetime(2023, 7, 12))
    comment150 = Comment(user_id=5, photo_id=59, text='Great composition', created_at=datetime(2023, 7, 12), updated_at=datetime(2023, 7, 12))

    comment151 = Comment(user_id=3, photo_id=59, text='Nice shot!', created_at=datetime(2023, 7, 12), updated_at=datetime(2023, 7, 12))
    comment152 = Comment(user_id=3, photo_id=60, text='Great composition', created_at=datetime(2023, 7, 12), updated_at=datetime(2023, 7, 12))
    comment153 = Comment(user_id=4, photo_id=60, text='Beautiful colors', created_at=datetime(2023, 7, 12), updated_at=datetime(2023, 7, 12))
    comment154 = Comment(user_id=2, photo_id=60, text='Fantastic shot!', created_at=datetime(2023, 7, 12), updated_at=datetime(2023, 7, 12))
    comment155 = Comment(user_id=9, photo_id=60, text='Impressive work', created_at=datetime(2023, 7, 12), updated_at=datetime(2023, 7, 12))
    comment156 = Comment(user_id=5, photo_id=61, text='Stunning view', created_at=datetime(2023, 7, 12), updated_at=datetime(2023, 7, 12))
    comment157 = Comment(user_id=1, photo_id=61, text='Lovely photo', created_at=datetime(2023, 7, 12), updated_at=datetime(2023, 7, 12))
    comment158 = Comment(user_id=7, photo_id=61, text='Impressive shot', created_at=datetime(2023, 7, 12), updated_at=datetime(2023, 7, 12))
    comment159 = Comment(user_id=3, photo_id=62, text='Fantastic job', created_at=datetime(2023, 7, 12), updated_at=datetime(2023, 7, 12))
    comment160 = Comment(user_id=10, photo_id=62, text='Wonderful composition', created_at=datetime(2023, 7, 12), updated_at=datetime(2023, 7, 12))
    comment161 = Comment(user_id=9, photo_id=63, text='Beautiful shot', created_at=datetime(2023, 7, 12), updated_at=datetime(2023, 7, 12))
    comment162 = Comment(user_id=4, photo_id=64, text='Captivating', created_at=datetime(2023, 7, 12), updated_at=datetime(2023, 7, 12))
    comment163 = Comment(user_id=3, photo_id=64, text='Breathtaking', created_at=datetime(2023, 7, 12), updated_at=datetime(2023, 7, 12))
    comment164 = Comment(user_id=2, photo_id=64, text='Wow!', created_at=datetime(2023, 7, 12), updated_at=datetime(2023, 7, 12))
    comment165 = Comment(user_id=8, photo_id=64, text='Outstanding work', created_at=datetime(2023, 7, 12), updated_at=datetime(2023, 7, 12))
    comment166 = Comment(user_id=8, photo_id=65, text='Incredible shot', created_at=datetime(2023, 7, 12), updated_at=datetime(2023, 7, 12))
    comment167 = Comment(user_id=1, photo_id=65, text='Lovely composition', created_at=datetime(2023, 7, 12), updated_at=datetime(2023, 7, 12))
    comment168 = Comment(user_id=5, photo_id=65, text='Nice shot!', created_at=datetime(2023, 7, 12), updated_at=datetime(2023, 7, 12))
    comment169 = Comment(user_id=3, photo_id=66, text='Great composition', created_at=datetime(2023, 7, 12), updated_at=datetime(2023, 7, 12))
    comment170 = Comment(user_id=8, photo_id=66, text='Beautiful colors', created_at=datetime(2023, 7, 12), updated_at=datetime(2023, 7, 12))
    comment171 = Comment(user_id=10, photo_id=66, text='Fantastic shot!', created_at=datetime(2023, 7, 12), updated_at=datetime(2023, 7, 12))
    comment172 = Comment(user_id=5, photo_id=66, text='Impressive', created_at=datetime(2023, 7, 12), updated_at=datetime(2023, 7, 12))
    comment173 = Comment(user_id=2, photo_id=66, text='Stunning view', created_at=datetime(2023, 7, 12), updated_at=datetime(2023, 7, 12))
    comment174 = Comment(user_id=1, photo_id=67, text='Lovely photo', created_at=datetime(2023, 7, 12), updated_at=datetime(2023, 7, 12))
    comment175 = Comment(user_id=3, photo_id=67, text='Impressive shot', created_at=datetime(2023, 7, 12), updated_at=datetime(2023, 7, 12))
    comment176 = Comment(user_id=8, photo_id=68, text='Fantastic job', created_at=datetime(2023, 7, 12), updated_at=datetime(2023, 7, 12))
    comment177 = Comment(user_id=6, photo_id=68, text='Wonderful composition', created_at=datetime(2023, 7, 12), updated_at=datetime(2023, 7, 12))
    comment178 = Comment(user_id=1, photo_id=68, text='Beautiful shot', created_at=datetime(2023, 7, 12), updated_at=datetime(2023, 7, 12))
    comment179 = Comment(user_id=10, photo_id=68, text='Captivating', created_at=datetime(2023, 7, 12), updated_at=datetime(2023, 7, 12))
    comment180 = Comment(user_id=1, photo_id=69, text='Breathtaking', created_at=datetime(2023, 7, 12), updated_at=datetime(2023, 7, 12))
    comment181 = Comment(user_id=3, photo_id=69, text='Wow!', created_at=datetime(2023, 7, 12), updated_at=datetime(2023, 7, 12))
    comment182 = Comment(user_id=5, photo_id=69, text='Outstanding work', created_at=datetime(2023, 7, 12), updated_at=datetime(2023, 7, 12))
    comment183 = Comment(user_id=2, photo_id=69, text='Incredible shot', created_at=datetime(2023, 7, 12), updated_at=datetime(2023, 7, 12))
    comment184 = Comment(user_id=9, photo_id=70, text='Lovely composition', created_at=datetime(2023, 7, 12), updated_at=datetime(2023, 7, 12))
    comment185 = Comment(user_id=6, photo_id=70, text='Nice shot!', created_at=datetime(2023, 7, 12), updated_at=datetime(2023, 7, 12))
    comment186 = Comment(user_id=4, photo_id=70, text='Great composition', created_at=datetime(2023, 7, 12), updated_at=datetime(2023, 7, 12))
    comment187 = Comment(user_id=2, photo_id=71, text='Beautiful colors', created_at=datetime(2023, 7, 12), updated_at=datetime(2023, 7, 12))
    comment188 = Comment(user_id=1, photo_id=71, text='Fantastic shot!', created_at=datetime(2023, 7, 12), updated_at=datetime(2023, 7, 12))
    comment189 = Comment(user_id=5, photo_id=72, text='Impressive work', created_at=datetime(2023, 7, 12), updated_at=datetime(2023, 7, 12))
    comment190 = Comment(user_id=3, photo_id=72, text='Stunning view', created_at=datetime(2023, 7, 12), updated_at=datetime(2023, 7, 12))
    comment191 = Comment(user_id=1, photo_id=72, text='Lovely photo', created_at=datetime(2023, 7, 12), updated_at=datetime(2023, 7, 12))
    comment192 = Comment(user_id=10, photo_id=73, text='Impressive shot', created_at=datetime(2023, 7, 12), updated_at=datetime(2023, 7, 12))
    comment193 = Comment(user_id=6, photo_id=73, text='Fantastic job', created_at=datetime(2023, 7, 12), updated_at=datetime(2023, 7, 12))
    comment194 = Comment(user_id=5, photo_id=73, text='Wonderful composition', created_at=datetime(2023, 7, 12), updated_at=datetime(2023, 7, 12))
    comment195 = Comment(user_id=3, photo_id=73, text='Beautiful shot', created_at=datetime(2023, 7, 12), updated_at=datetime(2023, 7, 12))
    comment196 = Comment(user_id=9, photo_id=74, text='Captivating', created_at=datetime(2023, 7, 12), updated_at=datetime(2023, 7, 12))
    comment197 = Comment(user_id=7, photo_id=74, text='Breathtaking', created_at=datetime(2023, 7, 12), updated_at=datetime(2023, 7, 12))
    comment198 = Comment(user_id=6, photo_id=74, text='Wow!', created_at=datetime(2023, 7, 12), updated_at=datetime(2023, 7, 12))
    comment199 = Comment(user_id=2, photo_id=74, text='Outstanding work', created_at=datetime(2023, 7, 12), updated_at=datetime(2023, 7, 12))
    comment200 = Comment(user_id=1, photo_id=75, text='Incredible shot', created_at=datetime(2023, 7, 12), updated_at=datetime(2023, 7, 12))

    comment201 = Comment(user_id=3, photo_id=75, text='Nice shot!', created_at=datetime(2023, 7, 12), updated_at=datetime(2023, 7, 12))
    comment202 = Comment(user_id=4, photo_id=75, text='Great composition', created_at=datetime(2023, 7, 12), updated_at=datetime(2023, 7, 12))
    comment203 = Comment(user_id=6, photo_id=75, text='Beautiful colors', created_at=datetime(2023, 7, 12), updated_at=datetime(2023, 7, 12))
    comment204 = Comment(user_id=10, photo_id=76, text='Fantastic shot!', created_at=datetime(2023, 7, 12), updated_at=datetime(2023, 7, 12))
    comment205 = Comment(user_id=1, photo_id=76, text='Impressive work', created_at=datetime(2023, 7, 12), updated_at=datetime(2023, 7, 12))
    comment206 = Comment(user_id=9, photo_id=76, text='Stunning view', created_at=datetime(2023, 7, 12), updated_at=datetime(2023, 7, 12))
    comment207 = Comment(user_id=10, photo_id=77, text='Lovely photo', created_at=datetime(2023, 7, 12), updated_at=datetime(2023, 7, 12))
    comment208 = Comment(user_id=3, photo_id=78, text='Impressive shot', created_at=datetime(2023, 7, 12), updated_at=datetime(2023, 7, 12))
    comment209 = Comment(user_id=1, photo_id=78, text='Fantastic job', created_at=datetime(2023, 7, 12), updated_at=datetime(2023, 7, 12))
    comment210 = Comment(user_id=9, photo_id=79, text='Wonderful composition', created_at=datetime(2023, 7, 12), updated_at=datetime(2023, 7, 12))
    comment211 = Comment(user_id=6, photo_id=79, text='Beautiful shot', created_at=datetime(2023, 7, 12), updated_at=datetime(2023, 7, 12))
    comment212 = Comment(user_id=7, photo_id=79, text='Captivating', created_at=datetime(2023, 7, 12), updated_at=datetime(2023, 7, 12))
    comment213 = Comment(user_id=2, photo_id=80, text='Breathtaking', created_at=datetime(2023, 7, 12), updated_at=datetime(2023, 7, 12))
    comment214 = Comment(user_id=3, photo_id=81, text='Wow!', created_at=datetime(2023, 7, 12), updated_at=datetime(2023, 7, 12))
    comment215 = Comment(user_id=4, photo_id=81, text='Outstanding work', created_at=datetime(2023, 7, 12), updated_at=datetime(2023, 7, 12))
    comment216 = Comment(user_id=7, photo_id=81, text='Incredible shot', created_at=datetime(2023, 7, 12), updated_at=datetime(2023, 7, 12))
    comment217 = Comment(user_id=10, photo_id=81, text='Lovely composition', created_at=datetime(2023, 7, 12), updated_at=datetime(2023, 7, 12))
    comment218 = Comment(user_id=2, photo_id=82, text='Nice shot!', created_at=datetime(2023, 7, 12), updated_at=datetime(2023, 7, 12))
    comment219 = Comment(user_id=9, photo_id=82, text='Great composition', created_at=datetime(2023, 7, 12), updated_at=datetime(2023, 7, 12))
    comment220 = Comment(user_id=4, photo_id=83, text='Beautiful colors', created_at=datetime(2023, 7, 12), updated_at=datetime(2023, 7, 12))
    comment221 = Comment(user_id=2, photo_id=83, text='Fantastic shot!', created_at=datetime(2023, 7, 12), updated_at=datetime(2023, 7, 12))
    comment222 = Comment(user_id=6, photo_id=83, text='Impressive', created_at=datetime(2023, 7, 12), updated_at=datetime(2023, 7, 12))
    comment223 = Comment(user_id=1, photo_id=84, text='Well done!', created_at=datetime(2023, 7, 12), updated_at=datetime(2023, 7, 12))
    comment224 = Comment(user_id=5, photo_id=84, text='Stunning view', created_at=datetime(2023, 7, 12), updated_at=datetime(2023, 7, 12))
    comment225 = Comment(user_id=3, photo_id=84, text='Lovely photo', created_at=datetime(2023, 7, 12), updated_at=datetime(2023, 7, 12))
    comment226 = Comment(user_id=2, photo_id=85, text='Impressive shot', created_at=datetime(2023, 7, 12), updated_at=datetime(2023, 7, 12))
    comment227 = Comment(user_id=10, photo_id=86, text='Fantastic job', created_at=datetime(2023, 7, 12), updated_at=datetime(2023, 7, 12))
    comment228 = Comment(user_id=6, photo_id=86, text='Wonderful composition', created_at=datetime(2023, 7, 12), updated_at=datetime(2023, 7, 12))
    comment229 = Comment(user_id=4, photo_id=87, text='Beautiful shot', created_at=datetime(2023, 7, 12), updated_at=datetime(2023, 7, 12))
    comment230 = Comment(user_id=7, photo_id=87, text='Captivating', created_at=datetime(2023, 7, 12), updated_at=datetime(2023, 7, 12))
    comment231 = Comment(user_id=8, photo_id=87, text='Breathtaking', created_at=datetime(2023, 7, 12), updated_at=datetime(2023, 7, 12))
    comment232 = Comment(user_id=1, photo_id=87, text='Wow!', created_at=datetime(2023, 7, 12), updated_at=datetime(2023, 7, 12))
    comment233 = Comment(user_id=2, photo_id=88, text='Outstanding work', created_at=datetime(2023, 7, 12), updated_at=datetime(2023, 7, 12))
    comment234 = Comment(user_id=5, photo_id=89, text='Incredible shot', created_at=datetime(2023, 7, 12), updated_at=datetime(2023, 7, 12))
    comment235 = Comment(user_id=2, photo_id=90, text='Lovely composition', created_at=datetime(2023, 7, 12), updated_at=datetime(2023, 7, 12))
    comment236 = Comment(user_id=8, photo_id=90, text='Nice shot!', created_at=datetime(2023, 7, 12), updated_at=datetime(2023, 7, 12))
    comment237 = Comment(user_id=7, photo_id=90, text='Great composition', created_at=datetime(2023, 7, 12), updated_at=datetime(2023, 7, 12))
    comment238 = Comment(user_id=3, photo_id=91, text='Beautiful colors', created_at=datetime(2023, 7, 12), updated_at=datetime(2023, 7, 12))
    comment239 = Comment(user_id=2, photo_id=91, text='Fantastic shot!', created_at=datetime(2023, 7, 12), updated_at=datetime(2023, 7, 12))
    comment240 = Comment(user_id=10, photo_id=91, text='Impressive', created_at=datetime(2023, 7, 12), updated_at=datetime(2023, 7, 12))
    comment241 = Comment(user_id=1, photo_id=91, text='Stunning view', created_at=datetime(2023, 7, 12), updated_at=datetime(2023, 7, 12))
    comment242 = Comment(user_id=6, photo_id=92, text='Lovely photo', created_at=datetime(2023, 7, 12), updated_at=datetime(2023, 7, 12))
    comment243 = Comment(user_id=3, photo_id=92, text='Impressive shot', created_at=datetime(2023, 7, 12), updated_at=datetime(2023, 7, 12))
    comment244 = Comment(user_id=5, photo_id=93, text='Fantastic job', created_at=datetime(2023, 7, 12), updated_at=datetime(2023, 7, 12))
    comment245 = Comment(user_id=4, photo_id=93, text='Wonderful composition', created_at=datetime(2023, 7, 12), updated_at=datetime(2023, 7, 12))
    comment246 = Comment(user_id=10, photo_id=93, text='Beautiful shot', created_at=datetime(2023, 7, 12), updated_at=datetime(2023, 7, 12))
    comment247 = Comment(user_id=6, photo_id=94, text='Captivating', created_at=datetime(2023, 7, 12), updated_at=datetime(2023, 7, 12))
    comment248 = Comment(user_id=2, photo_id=94, text='Breathtaking', created_at=datetime(2023, 7, 12), updated_at=datetime(2023, 7, 12))
    comment249 = Comment(user_id=7, photo_id=94, text='Wow!', created_at=datetime(2023, 7, 12), updated_at=datetime(2023, 7, 12))
    comment250 = Comment(user_id=8, photo_id=94, text='Outstanding work', created_at=datetime(2023, 7, 12), updated_at=datetime(2023, 7, 12))

    comment251 = Comment(user_id=5, photo_id=95, text='Nice shot!', created_at=datetime(2023, 7, 12), updated_at=datetime(2023, 7, 12))
    comment252 = Comment(user_id=3, photo_id=95, text='Great composition', created_at=datetime(2023, 7, 12), updated_at=datetime(2023, 7, 12))
    comment253 = Comment(user_id=1, photo_id=96, text='Beautiful colors', created_at=datetime(2023, 7, 12), updated_at=datetime(2023, 7, 12))
    comment254 = Comment(user_id=4, photo_id=96, text='Fantastic shot!', created_at=datetime(2023, 7, 12), updated_at=datetime(2023, 7, 12))
    comment255 = Comment(user_id=8, photo_id=97, text='Impressive work', created_at=datetime(2023, 7, 12), updated_at=datetime(2023, 7, 12))
    comment256 = Comment(user_id=6, photo_id=97, text='Stunning view', created_at=datetime(2023, 7, 12), updated_at=datetime(2023, 7, 12))
    comment257 = Comment(user_id=1, photo_id=97, text='Lovely photo', created_at=datetime(2023, 7, 12), updated_at=datetime(2023, 7, 12))
    comment258 = Comment(user_id=7, photo_id=97, text='Impressive shot', created_at=datetime(2023, 7, 12), updated_at=datetime(2023, 7, 12))
    comment259 = Comment(user_id=6, photo_id=98, text='Fantastic job', created_at=datetime(2023, 7, 12), updated_at=datetime(2023, 7, 12))
    comment260 = Comment(user_id=2, photo_id=98, text='Wonderful composition', created_at=datetime(2023, 7, 12), updated_at=datetime(2023, 7, 12))
    comment261 = Comment(user_id=3, photo_id=98, text='Beautiful shot', created_at=datetime(2023, 7, 12), updated_at=datetime(2023, 7, 12))
    comment262 = Comment(user_id=9, photo_id=99, text='Captivating', created_at=datetime(2023, 7, 12), updated_at=datetime(2023, 7, 12))
    comment263 = Comment(user_id=4, photo_id=99, text='Breathtaking', created_at=datetime(2023, 7, 12), updated_at=datetime(2023, 7, 12))
    comment264 = Comment(user_id=8, photo_id=99, text='Wow!', created_at=datetime(2023, 7, 12), updated_at=datetime(2023, 7, 12))
    comment265 = Comment(user_id=6, photo_id=100, text='Outstanding work', created_at=datetime(2023, 7, 12), updated_at=datetime(2023, 7, 12))
    comment266 = Comment(user_id=1, photo_id=101, text='Incredible shot', created_at=datetime(2023, 7, 12), updated_at=datetime(2023, 7, 12))
    comment267 = Comment(user_id=9, photo_id=101, text='Lovely composition', created_at=datetime(2023, 7, 12), updated_at=datetime(2023, 7, 12))
    comment268 = Comment(user_id=3, photo_id=102, text='Nice shot!', created_at=datetime(2023, 7, 12), updated_at=datetime(2023, 7, 12))
    comment269 = Comment(user_id=2, photo_id=102, text='Great composition', created_at=datetime(2023, 7, 12), updated_at=datetime(2023, 7, 12))
    comment270 = Comment(user_id=4, photo_id=102, text='Beautiful colors', created_at=datetime(2023, 7, 12), updated_at=datetime(2023, 7, 12))
    comment271 = Comment(user_id=8, photo_id=102, text='Fantastic shot!', created_at=datetime(2023, 7, 12), updated_at=datetime(2023, 7, 12))
    comment272 = Comment(user_id=6, photo_id=103, text='Impressive work', created_at=datetime(2023, 7, 12), updated_at=datetime(2023, 7, 12))
    comment273 = Comment(user_id=1, photo_id=104, text='Stunning view', created_at=datetime(2023, 7, 12), updated_at=datetime(2023, 7, 12))
    comment274 = Comment(user_id=9, photo_id=104, text='Lovely photo', created_at=datetime(2023, 7, 12), updated_at=datetime(2023, 7, 12))
    comment275 = Comment(user_id=3, photo_id=105, text='Impressive shot', created_at=datetime(2023, 7, 12), updated_at=datetime(2023, 7, 12))
    comment276 = Comment(user_id=8, photo_id=105, text='Fantastic job', created_at=datetime(2023, 7, 12), updated_at=datetime(2023, 7, 12))
    comment277 = Comment(user_id=7, photo_id=105, text='Wonderful composition', created_at=datetime(2023, 7, 12), updated_at=datetime(2023, 7, 12))
    comment278 = Comment(user_id=4, photo_id=106, text='Beautiful shot', created_at=datetime(2023, 7, 12), updated_at=datetime(2023, 7, 12))
    comment279 = Comment(user_id=1, photo_id=106, text='Captivating', created_at=datetime(2023, 7, 12), updated_at=datetime(2023, 7, 12))
    comment280 = Comment(user_id=9, photo_id=106, text='Breathtaking', created_at=datetime(2023, 7, 12), updated_at=datetime(2023, 7, 12))
    comment281 = Comment(user_id=3, photo_id=107, text='Wow!', created_at=datetime(2023, 7, 12), updated_at=datetime(2023, 7, 12))
    comment282 = Comment(user_id=2, photo_id=107, text='Outstanding work', created_at=datetime(2023, 7, 12), updated_at=datetime(2023, 7, 12))
    comment283 = Comment(user_id=8, photo_id=107, text='Incredible shot', created_at=datetime(2023, 7, 12), updated_at=datetime(2023, 7, 12))
    comment284 = Comment(user_id=5, photo_id=108, text='Lovely composition', created_at=datetime(2023, 7, 12), updated_at=datetime(2023, 7, 12))
    comment285 = Comment(user_id=1, photo_id=108, text='Nice shot!', created_at=datetime(2023, 7, 12), updated_at=datetime(2023, 7, 12))
    comment286 = Comment(user_id=9, photo_id=108, text='Great composition', created_at=datetime(2023, 7, 12), updated_at=datetime(2023, 7, 12))
    comment287 = Comment(user_id=2, photo_id=108, text='Beautiful colors', created_at=datetime(2023, 7, 12), updated_at=datetime(2023, 7, 12))
    comment288 = Comment(user_id=7, photo_id=109, text='Fantastic shot!', created_at=datetime(2023, 7, 12), updated_at=datetime(2023, 7, 12))
    comment289 = Comment(user_id=4, photo_id=109, text='Impressive work', created_at=datetime(2023, 7, 12), updated_at=datetime(2023, 7, 12))
    comment290 = Comment(user_id=6, photo_id=109, text='Stunning view', created_at=datetime(2023, 7, 12), updated_at=datetime(2023, 7, 12))
    comment291 = Comment(user_id=7, photo_id=110, text='Lovely photo', created_at=datetime(2023, 7, 12), updated_at=datetime(2023, 7, 12))
    comment292 = Comment(user_id=1, photo_id=110, text='Impressive shot', created_at=datetime(2023, 7, 12), updated_at=datetime(2023, 7, 12))
    comment293 = Comment(user_id=5, photo_id=111, text='Fantastic job', created_at=datetime(2023, 7, 12), updated_at=datetime(2023, 7, 12))
    comment294 = Comment(user_id=8, photo_id=111, text='Wonderful composition', created_at=datetime(2023, 7, 12), updated_at=datetime(2023, 7, 12))
    comment295 = Comment(user_id=2, photo_id=111, text='Beautiful shot', created_at=datetime(2023, 7, 12), updated_at=datetime(2023, 7, 12))
    comment296 = Comment(user_id=3, photo_id=111, text='Captivating', created_at=datetime(2023, 7, 12), updated_at=datetime(2023, 7, 12))
    comment297 = Comment(user_id=4, photo_id=112, text='Breathtaking', created_at=datetime(2023, 7, 12), updated_at=datetime(2023, 7, 12))
    comment298 = Comment(user_id=7, photo_id=112, text='Wow!', created_at=datetime(2023, 7, 12), updated_at=datetime(2023, 7, 12))
    comment299 = Comment(user_id=8, photo_id=112, text='Outstanding work', created_at=datetime(2023, 7, 12), updated_at=datetime(2023, 7, 12))
    comment300 = Comment(user_id=6, photo_id=113, text='Incredible shot', created_at=datetime(2023, 7, 12), updated_at=datetime(2023, 7, 12))
    comment301 = Comment(user_id=1, photo_id=113, text='Lovely composition', created_at=datetime(2023, 7, 12), updated_at=datetime(2023, 7, 12))
    comment302 = Comment(user_id=3, photo_id=113, text='Nice shot!', created_at=datetime(2023, 7, 12), updated_at=datetime(2023, 7, 12))
    comment303 = Comment(user_id=9, photo_id=114, text='Great composition', created_at=datetime(2023, 7, 12), updated_at=datetime(2023, 7, 12))
    comment304 = Comment(user_id=4, photo_id=115, text='Beautiful colors', created_at=datetime(2023, 7, 12), updated_at=datetime(2023, 7, 12))
    comment305 = Comment(user_id=8, photo_id=115, text='Fantastic shot!', created_at=datetime(2023, 7, 12), updated_at=datetime(2023, 7, 12))

    all_comments = [comment1, comment2, comment3, comment4, comment5, comment6, comment7, comment8, comment9, comment10,
                    comment11, comment12, comment13, comment14, comment15, comment16, comment17, comment18, comment19, comment20,
                    comment21, comment22, comment23, comment24, comment25, comment26, comment27, comment28, comment29, comment30,
                    comment31, comment32, comment33, comment34, comment35, comment36, comment37, comment38, comment39, comment40,
                    comment41, comment42, comment43, comment44, comment45, comment46, comment47, comment48, comment49, comment50,
                    comment51, comment52, comment53, comment54, comment55, comment56, comment57, comment58, comment59, comment60,
                    comment61, comment62, comment63, comment64, comment65, comment66, comment67, comment68, comment69, comment70,
                    comment71, comment72, comment73, comment74, comment75, comment76, comment77, comment78, comment79, comment80,
                    comment81, comment82, comment83, comment84, comment85, comment86, comment87, comment88, comment89, comment90,
                    comment91, comment92, comment93, comment94, comment95, comment96, comment97, comment98, comment99, comment100,
                    comment101, comment102, comment103, comment104, comment105, comment106, comment107, comment108, comment109, comment110,
                    comment111, comment112, comment113, comment114, comment115, comment116, comment117, comment118, comment119, comment120,
                    comment121, comment122, comment123, comment124, comment125, comment126, comment127, comment128, comment129, comment130,
                    comment131, comment132, comment133, comment134, comment135, comment136, comment137, comment138, comment139, comment140,
                    comment141, comment142, comment143, comment144, comment145, comment146, comment147, comment148, comment149, comment150,
                    comment151, comment152, comment153, comment154, comment155, comment156, comment157, comment158, comment159, comment160,
                    comment161, comment162, comment163, comment164, comment165, comment166, comment167, comment168, comment169, comment170,
                    comment171, comment172, comment173, comment174, comment175, comment176, comment177, comment178, comment179, comment180,
                    comment181, comment182, comment183, comment184, comment185, comment186, comment187, comment188, comment189, comment190,
                    comment191, comment192, comment193, comment194, comment195, comment196, comment197, comment198, comment199, comment200,
                    comment201, comment202, comment203, comment204, comment205, comment206, comment207, comment208, comment209, comment210,
                    comment211, comment212, comment213, comment214, comment215, comment216, comment217, comment218, comment219, comment220,
                    comment221, comment222, comment223, comment224, comment225, comment226, comment227, comment228, comment229, comment230,
                    comment231, comment232, comment233, comment234, comment235, comment236, comment237, comment238, comment239, comment240,
                    comment241, comment242, comment243, comment244, comment245, comment246, comment247, comment248, comment249, comment250,
                    comment251, comment252, comment253, comment254, comment255, comment256, comment257, comment258, comment259, comment260,
                    comment261, comment262, comment263, comment264, comment265, comment266, comment267, comment268, comment269, comment270,
                    comment271, comment272, comment273, comment274, comment275, comment276, comment277, comment278, comment279, comment280,
                    comment281, comment282, comment283, comment284, comment285, comment286, comment287, comment288, comment289, comment290,
                    comment291, comment292, comment293, comment294, comment295, comment296, comment297, comment298, comment299, comment300,
                    comment301, comment302, comment303, comment304, comment305
                    ]

    _ = [db.session.add(comment) for comment in all_comments]
    db.session.commit()


# Uses a raw SQL query to TRUNCATE or DELETE the comments table. SQLAlchemy doesn't
# have a built in function to do this. With postgres in production TRUNCATE
# removes all the data from the table, and RESET IDENTITY resets the auto
# incrementing primary key, CASCADE deletes any dependent entities.  With
# sqlite3 in development you need to instead use DELETE to remove all data and
# it will reset the primary keys for you as well.
def undo_comments():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.comments RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM comments"))

    db.session.commit()
