from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField, EmailField
from wtforms.validators import DataRequired


class AddJobForm(FlaskForm):
    teamleader_id = IntegerField('Team Leader id', validators=[DataRequired()])
    job = StringField('Job description', validators=[DataRequired()])
    work_size = IntegerField('Work size', validators=[DataRequired()])
    collaborators = StringField('Collaborators ids', validators=[DataRequired()])
    # end_date = StringField('End date', validators=[DataRequired()])
    is_finished = BooleanField('Is job finished?')
    submit = SubmitField('Add')