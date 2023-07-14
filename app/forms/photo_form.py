# from flask_wtf import FlaskForm
# from flask_wtf.file import FileField, FileAllowed, FileRequired
# from wtforms.validators import DataRequired, Length, URL
# from wtforms import SubmitField, StringField, DateField
# from ..api.AWS_helpers import ALLOWED_EXTENSIONS

# class PhotoForm(FlaskForm):
#     #id automatically assigned
#     #user_id taken from current user
#     photo = FileField("Image File", validators=[FileRequired(), FileAllowed(list(ALLOWED_EXTENSIONS))])
#     title = StringField()
#     description = StringField()
#     taken_at = DateField()
#     #created_at = now
#     submit = SubmitField("Submit")
