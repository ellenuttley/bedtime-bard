"""This file contains forms for the signup process"""
from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, PasswordField, SelectMultipleField, SubmitField
from wtforms.validators import DataRequired, Length, Regexp

# I know some of these lines are too long, but I thought in terms of readability it made more sense to have one field
# per line - Ellen


# Registration step : 1 / 3 - enters information into the User model
# Route : signup
class NewUserForm(FlaskForm):
    username = StringField('Username', validators=[Regexp('^[a-zA-Z\d_\.-]+$', message="Please use only numbers, letters, and the following symbols : . - _"), DataRequired(), Length(min=1, max=50)])
    password = PasswordField('Password', validators=[Regexp('^[a-zA-Z\d_\.-]+$'), DataRequired()])
    # The above contain regex validators to make sure the input is one word, and contains only numbers letters and certain strings

    name = StringField("Child's Name", validators=[DataRequired(), Length(min=1, max=50)])
    # name = StringField("Child's Name", validators=[Regexp('^[a-zA-Z]+$', message="Please use only numbers, letters, and the following symbols : . - _"), DataRequired(), Length(min=1, max=50)])
    age = SelectField("Child's Age", choices=[(i, str(i)) for i in range(1, 18)], validators=[DataRequired()])
    pronouns = SelectField('Pronouns', choices=['She/Her', 'He/Him', 'They/Them'], validators=[DataRequired()])

    # The above contained descriptions, that provide information for sibling groups :
    # Name - description="For siblings, please input all of their names separated by 'and' :)"
    # Age - description="Please select the age of the youngest sibling",
    # Pronouns - description="For siblings of different genders, please select 'They / Them'"

    submit = SubmitField("Let's Go!")


# Registration step : 2 / 3 - enters information into the User StoryTypes / Dislikes / Creature models
# Route : story_elements
class ChooseStoryElements(FlaskForm):
    creature_choices = SelectMultipleField('What kinds of creatures do you like stories about?', validators=[DataRequired()])
    story_type_choices = SelectMultipleField('What types of stories do you like?', validators=[DataRequired()])
    dislikes_choices = SelectMultipleField('What types of stories do you not like?')

    submit = SubmitField('Whoop Whoop!')


# Registration step : 3 / 3 - enters information into the UserBedtimeRoutine model
# Route : bedtime_steps
class BedtimeRoutineForm(FlaskForm):

    bedtime_step_1 = SelectField('Bedtime Step 1:', validators=[DataRequired()])
    bedtime_step_2 = SelectField('Bedtime Step 2:', validators=[DataRequired()])
    bedtime_step_3 = SelectField('Bedtime Step 3:', validators=[DataRequired()])
    bedtime_step_4 = SelectField('Bedtime Step 4:', validators=[DataRequired()])
    bedtime_step_5 = SelectField('Bedtime Step 5:', validators=[DataRequired()])

    submit = SubmitField('Done!')
