from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed, FileRequired
from app.api.AWS_helpers import ALLOWED_EXTENSIONS
from wtforms import StringField, DateField, SubmitField
from wtforms.validators import DataRequired

class PhotoForm(FlaskForm):
    #id generated
    #user_id is current user
    photo = FileField('Photo File', validators = [FileRequired(), FileAllowed(list(ALLOWED_EXTENSIONS))])
    title = StringField('Title', validators = [DataRequired()])
    description = StringField('Description', validators = [DataRequired()])
    taken_at = DateField('Date', validators = [DataRequired()])
    #created_at is date.now()
    submit = SubmitField('Submit')
