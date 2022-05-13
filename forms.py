from flask_wtf import FlaskForm
from wtforms.fields import StringField , PasswordField , EmailField , SubmitField
from wtforms.validators import DataRequired , Email

class GetDataForm(FlaskForm):
    # <input type='text' name='firstname'>
    firstname = StringField(validators=[DataRequired('First name is required ')])
    email = EmailField(validators=[DataRequired('Email is Required .') , Email('EMail is InValid')]) # input:email
    submit = SubmitField('Click Me')

