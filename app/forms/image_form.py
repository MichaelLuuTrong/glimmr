from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms.validators import DataRequired, Length, URL
from wtforms import SubmitField
from app.routes.aws_helpers import ALLOWED_EXTENSIONS

class ImageForm(FlaskForm):
    image = FileField("Image File", validators=[FileRequired(), FileAllowed(list(ALLOWED_EXTENSIONS))])
    title = TextField()
    description = TextField()
    taken_at = DateField()
    submit = SubmitField("Submit")
