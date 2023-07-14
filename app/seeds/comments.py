from app.models import db, Comment, environment, SCHEMA
from sqlalchemy.sql import text
from datetime import datetime

def seed_comments():
    comment1 = Comment(
        user_id=1,
        photo_id=8,
        text='Animals are so beautiful close-up!',
        created_at=datetime(2023, 7, 12),
        updated_at=datetime(2023, 7, 12)
    )
    comment2 = Comment(
        user_id=1,
        photo_id=9,
        text='There must be so many beautiful animals that are unidentified. Thank you for sharing!',
        created_at=datetime(2023, 7, 13),
        updated_at=datetime(2023, 7, 13)
    )
    comment3 = Comment(
        user_id=1,
        photo_id=12,
        text='Amazing colors!',
        created_at=datetime(2023, 7, 14),
        updated_at=datetime(2023, 7, 14)
    )
    comment4 = Comment(
        user_id=2,
        photo_id=1,
        text='I love the layers.',
        created_at=datetime(2023, 7, 12),
        updated_at=datetime(2023, 7, 12)
    )
    comment5 = Comment(
        user_id=2,
        photo_id=3,
        text='Hot air balloons are beautiful from the ground, but even moreso from the air',
        created_at=datetime(2023, 7, 13),
        updated_at=datetime(2023, 7, 13)
    )
    comment6 = Comment(
        user_id=2,
        photo_id=13,
        text='Amazing shot!',
        created_at=datetime(2023, 7, 14),
        updated_at=datetime(2023, 7, 14)
    )
    comment7 = Comment(
        user_id=3,
        photo_id=2,
        text='I love the colors of autumn',
        created_at=datetime(2023, 7, 12),
        updated_at=datetime(2023, 7, 12)
    )
    comment8 = Comment(
        user_id=3,
        photo_id=5,
        text='I love this series. Keep up the great work!',
        created_at=datetime(2023, 7, 13),
        updated_at=datetime(2023, 7, 13)
    )
    comment9 = Comment(
        user_id=3,
        photo_id=4,
        text='Seeing things from an aerial perspective is so amazing and different. Thank you for sharing!',
        created_at=datetime(2023, 7, 14),
        updated_at=datetime(2023, 7, 14)
    )

    all_comments = [comment1, comment2, comment3, comment4,
                    comment5, comment6, comment7, comment8,
                    comment9]

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
