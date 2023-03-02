from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    astronaut_id = IntegerField('Id астронавта', validators=[DataRequired()])
    astronaut_password = StringField('Пароль астронавта', validators=[DataRequired()])
    captain_id = IntegerField('Id капитана', validators=[DataRequired()])
    captain_password = StringField('Пароль капитана', validators=[DataRequired()])
    submit = SubmitField('Доступ')