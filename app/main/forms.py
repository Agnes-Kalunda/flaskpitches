from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField,SelectField
from wtforms.validators import DataRequired

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Who am I ?.', validators=[DataRequired()])
    submit = SubmitField("Save changes")
class PitchForm(FlaskForm):
    title = StringField('Title', validators = [DataRequired()])
    pitch = TextAreaField('Pitch')
    category = SelectField('Pitch Category', choices=[('Elevator','Elevator'),('Interview','Interview'),('Adding a Contact','Adding a Contact'),('Job Opportunity','Job Opportunity'), ('Product Pitch','Product Pitch'),('Promotional Pitch','Promotional Pitch')])
    submit = SubmitField('Add pitch')
class CommentForm(FlaskForm):
    title = StringField('Title', validators = [DataRequired()])
    comment = TextAreaField('Comment')
    submit = SubmitField('Add comment')