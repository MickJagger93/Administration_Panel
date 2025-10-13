import re
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, IntegerField, TextAreaField
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError

def strong_password (form, field):
    password = field.data
    if len(re.findall(r'[0-9]', password)) < 2:
        raise ValidationError('Password must contain at least 2 numbers.')
    if len(re.findall(r'[A-Za-z]', password)) < 2:
        raise ValidationError('Password must contain at least 2 letters.')
    if len(re.findall(r'[^A-Za-z0-9]', password)) < 2:
        raise ValidationError('Password must contain at least 2 special characters.')

class LoginForm(FlaskForm):

    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), strong_password])
    submit = SubmitField('Log in')

class RegisterForm(FlaskForm):

    name = StringField('Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), strong_password])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), strong_password])
    remember_password = BooleanField('Remember Password')
    submit = SubmitField('Register')

class ResetForm(FlaskForm):

    email = StringField('Email', validators=[DataRequired()])
    new_password = PasswordField('New Password', validators=[DataRequired(), strong_password])
    confirm_new_password = PasswordField('Confirm New Password', validators=[DataRequired(), EqualTo('new_password'), strong_password])
    submit = SubmitField('Reset Password')

class ProductForm(FlaskForm):

    name_product = StringField('Name Product', validators=[DataRequired()])
    price = IntegerField('Price', validators=[DataRequired()])
    description = StringField('Description', validators=[DataRequired()])
    category = StringField('Category', validators=[DataRequired()])

class EditProduct(FlaskForm):

    name_product = StringField('Name Product', validators=[DataRequired()])
    price = IntegerField('Price', validators=[DataRequired()])
    description = StringField('Description', validators=[DataRequired()])
    category = StringField('Category', validators=[DataRequired()])

class PostForm(FlaskForm):

    name_post = StringField('Name Post', validators=[DataRequired()])
    post = TextAreaField('Post', validators=[DataRequired()])
    date = StringField('Date', validators=[DataRequired()])
    category = StringField('Category', validators=[DataRequired()])
    submit = SubmitField('Send Post')

class EditPost(FlaskForm):

    name_post = StringField('Name Post', validators=[DataRequired()])
    post = TextAreaField('Post', validators=[DataRequired()])
    date = StringField('Date', validators=[DataRequired()])
    category = StringField('Category', validators=[DataRequired()])