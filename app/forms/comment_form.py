from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class CommentForm(FlaskForm):
    #id is generated
    #user_id from current user
    #photo_id from current photo
    text = StringField('Insert Comment Here', validators = [DataRequired()])
    #created at is datetime.now()
    #updated_at is datetime.now()
    submit = SubmitField('Submit')
