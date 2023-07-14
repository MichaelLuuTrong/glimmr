from flask_wtf import FlaskForm
from wtforms import StringField, DateField, SubmitField
from wtforms.validators import DataRequired

class PhotoForm(FlaskForm):
    #id generated
    #user_id is current user
    photo = StringField('Photo URL', validators = [DataRequired()])
    title = StringField('Title', validators = [DataRequired()])
    description = StringField('Description', validators = [DataRequired()])
    taken_at = DateField('Date', validators = [DataRequired()])
    #created_at is date.now()
    submit = SubmitField('Submit')
