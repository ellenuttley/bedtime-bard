"""
This page contains our database models, including methods for informing the prompt generation.
The password should be / was hashed - but we had myriad issues with the database and this change ended up being rolled
back, and we didn't get a chance to properly implement it again. So, you may also see remnants of this elsewhere.

I know some of these lines are too long - but it made more sense to me to keep it one variable per line - Ellen
"""

from . import db
from sqlalchemy import func
from sqlalchemy.orm import aliased
from flask_login import UserMixin
import bcrypt                                                  # for password hashing that isn't currently implemented


# This model contains all the users personal information, obtained via the NewUserForm
# Registration step : 1 / 3
# It is used throughout the app for authenticating the current user
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(100), nullable=False)       # password should be hashed
    name = db.Column(db.String(80), nullable=False)
    age = db.Column(db.Integer)
    pronouns = db.Column(db.String(100), nullable=False)

    # Foreign keys - creates a network to allow other models access to the current User information :
    bedtime_steps = db.relationship('UserBedtimeRoutine', backref='bedtime_user', primaryjoin='User.id==UserBedtimeRoutine.user_id', lazy=True)
    user_creatures = db.relationship('UserCreature', backref='user_creature', primaryjoin='User.id==UserCreature.user_id', lazy=True)
    user_story_type = db.relationship('UserStoryType', backref='user_story', primaryjoin='User.id==UserStoryType.user_id', lazy=True)
    user_dislikes = db.relationship('UserDislike', backref='user_dislikes', primaryjoin='User.id==UserDislike.user_id', lazy=True)

    # Method to get the current user.id :
    def get_id(self):
        return str(self.id)

    # Method to check whether the user is logged in / authenticated :
    def is_authenticated(self):
        return True

# ---------- METHODS FOR AI STORY PROMPT GENERATION -------------------------------------------------------------------
# Story Generation Step : 1 -- Full generation process in story_generation route in routes.py -------------------------

# These methods use the foreign key network mentioned above to retrieve data to inform the AI prompts
# They also include various exception handling fail-safes, to try and ensure that even if the data is invalid the child
# gets a readable story

    # Returns the current users name / names
    # If name is None or less than 1 letter, it returns 'Super Kid!' to be used in the prompt instead
    def get_name(self):
        if self.name and len(self.name) > 1:
            return self.name
        else:
            return 'Super Kid!'

    # Returns the current users pronouns
    # If pronouns is None returns They/Them
    def get_pronouns(self):
        if self.pronouns:
            return self.pronouns
        else:
            return 'They/Them'

    # Returns the age saved for the current users account
    # If age is None it returns 5 - so the prompt would generate a story suitable for a young child
    def get_age(self):
        if self.age:
            return self.age
        else:
            return 5

    # This method to gets a random story type from the users preferences - which are stored in the UserStoryType table
    # It then uses the foreign key relationship with the StoryTypeChoices table to return the label for it
    # this label is then returned to be fed to the prompt
    # If the random story type returns None, it chooses one from the entire StoryTypeChoices table at random
    def get_story_type(self):
        random_story_type = UserStoryType.query.filter_by(user_id=self.id).order_by(func.random()).first()
        if random_story_type:
            story_type = random_story_type.story_type_choices.label
        else:
            random_story_choice = StoryTypeChoice.query.order_by(func.random()).first()
            story_type = random_story_choice.label if random_story_choice else None

        return story_type

    # This method does the same as above, but with Creature :
    def get_creature(self):
        random_creature = UserCreature.query.filter_by(user_id=self.id).order_by(func.random()).first()
        if random_creature:
            creature = random_creature.creature_choices.label
        else:
            random_creature_choice = CreatureChoice.query.order_by(func.random()).first()
            creature = random_creature_choice.label if random_creature_choice else None

        return creature

    # This method to get all the users dislikes for story content - which are stored in the UserDislikes table
    # It then uses the foreign key relationship with the DislikeChoices table to return the label for each of them
    # these labels are concatenated into a string separated by commas - which is then returned to be fed to the prompt
    # If dislikes returns None, it returns a blank string
    def get_dislikes(self):
        dislikes = ', '.join([dislike.dislike_choices.label if dislike.dislike_choices
                        else "" for dislike in UserDislike.query.filter_by(user_id=self.id).all()]) or ""

        return dislikes

    # This method to get all the users bedtime routine steps - which are stored in the UserBedtimeRoutine table
    # It then uses the foreign key relationship with the BedtimeSteps table to return the label for each of them
    # these labels are then added to a list - which is then returned to be fed to the prompt
    # If a bedtime step returns None, it'll add 'Do Something!' to the prompts list - so the popup is still encouraging,
    # functional and appropriate
    def get_routine(self):
        bedtime_routine = [
            bedtime_step.bedtime_steps.label if bedtime_step.bedtime_steps else "Do Something!"
            for position in range(1, 6)
            for bedtime_step in UserBedtimeRoutine.query.filter_by(user_id=self.id, position=position).all()
            if bedtime_step.bedtime_steps.label
        ]
        return bedtime_routine

    def __repr__(self):
        return f'<{self.name}>'

# ---------------------------------------------------------------------------------------------------------------------
# ---- BEDTIME ROUTINE MODELS -----------------------------------------------------------------------------
# Model that stores all the available choices for bedtime routine steps.
# These are then populated as choices in the BedtimeRoutineForm - Registration step : 3 / 3
class BedtimeSteps(db.Model, UserMixin):
    __tablename__ = 'bedtime_steps'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    label = db.Column(db.String(255), nullable=False)

    # Foreign key relationship with the UserBedtimeRoutine model
    # Used in the get_routine method in the User model
    bedtime_steps = db.relationship('UserBedtimeRoutine', backref='bedtime_choices_id',
                                    primaryjoin='BedtimeSteps.id==UserBedtimeRoutine.bedtime_step_id', lazy=True)

    def __str__(self):
        return self.label


# Model stores the bedtime steps chosen by the user in the BedtimeRoutineForm above
class UserBedtimeRoutine(db.Model, UserMixin):
    __tablename__ = 'user_bedtime_routine'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey(User.id), nullable=False)
    bedtime_step_id = db.Column(db.Integer, db.ForeignKey(BedtimeSteps.id), nullable=False)
    position = db.Column(db.Integer, nullable=False)

    # Foreign key relationships with the User and UserBedtimeRoutine models.
    # Used by the get_routine method in the User model
    user = db.relationship('User', foreign_keys='UserBedtimeRoutine.user_id', overlaps="bedtime_steps,bedtime_user")
    bedtime_steps = db.relationship('BedtimeSteps', foreign_keys='UserBedtimeRoutine.bedtime_step_id',
                                    overlaps="bedtime_choices_id, bedtime_steps")

    def __str__(self):
        return self.label

# ---------------------------------------------------------------------------------------------------------------------
# ---- STORY TYPE MODELS -----------------------------------------------------------------------------
# Model that stores all the available story type choices.
# These are populated as options in the story_type_choices field of the ChooseStoryElementsForm
# Registration step : 2 / 3
class StoryTypeChoice(db.Model, UserMixin):
    __tablename__ = 'story_type_choices'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    label = db.Column(db.String(32), nullable=False)

    # Foreign key relationship with the UserStoryType model. Used in the get_story_type method in the User model
    story_type_id = db.relationship('UserStoryType', backref='type_id',
                                    primaryjoin='StoryTypeChoice.id==UserStoryType.story_type_id', lazy=True)

    def __str__(self):
        return self.label


# Model stores the story types chosen by the user in the ChooseStoryElementsForm above
class UserStoryType(db.Model, UserMixin):
    __tablename__ = 'user_story_types'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey(User.id), nullable=False)
    story_type_id = db.Column(db.Integer, db.ForeignKey(StoryTypeChoice.id), nullable=False)

    # Foreign key relationships with the User and StoryTypeChoice models.
    # Used by the get_story_type method in the User model
    user = db.relationship('User', foreign_keys='UserStoryType.user_id', overlaps="user_story,user_story_type")
    story_type_choices = db.relationship('StoryTypeChoice', foreign_keys='UserStoryType.story_type_id',
                                         overlaps="story_type_id,type_id")

    def __str__(self):
        return self.label

# ---------------------------------------------------------------------------------------------------------------------
# ---- CREATURE MODELS -----------------------------------------------------------------------------
# Model that stores all the available creature choices.
# These are populated as options in the creature_choices field of the ChooseStoryElementsForm
# Registration step : 2 / 3
class CreatureChoice(db.Model, UserMixin):
    __tablename__ = 'creature_choices'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    label = db.Column(db.String(32), nullable=False)

    creature_id = db.relationship('UserCreature', backref='creature_choices_id',
                                  primaryjoin='CreatureChoice.id==UserCreature.creature_id', lazy=True)

    def __str__(self):
        return self.label


# Model stores the creatures chosen by the user in the ChooseStoryElementsForm above
class UserCreature(db.Model, UserMixin):
    __tablename__ = 'user_creatures'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey(User.id), nullable=False)
    creature_id = db.Column(db.Integer, db.ForeignKey(CreatureChoice.id), nullable=False)

    # Foreign key relationships with the User and CreatureChoice models.
    # Used by the get_creature method in the User model
    user = db.relationship('User', foreign_keys='UserCreature.user_id', overlaps="user_creature,user_creatures")
    creature_choices = db.relationship('CreatureChoice', foreign_keys='UserCreature.creature_id',
                                       overlaps="creature_choices_id,creature_id")


    def __str__(self):
        return self.label

# ---------------------------------------------------------------------------------------------------------------------
# ---- DISLIKE MODELS -----------------------------------------------------------------------------
# Model that stores all the available dislike choices.
# These are populated as options in the dislike_choices field of the ChooseStoryElementsForm
# Registration step : 2 / 3
class DislikeChoice(db.Model, UserMixin):
    __tablename__ = 'dislike_choices'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    label = db.Column(db.String(32), nullable=False)

    user_dislikes = db.relationship('UserDislike', backref='dislike_choices_id',
                                    primaryjoin='DislikeChoice.id==UserDislike.dislike_id', lazy=True)

    def __str__(self):
        return self.label


# Model stores the dislikes chosen by the user in the ChooseStoryElementsForm above
class UserDislike(db.Model, UserMixin):
    __tablename__ = 'user_dislikes'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey(User.id), nullable=False)
    dislike_id = db.Column(db.Integer, db.ForeignKey(DislikeChoice.id), nullable=False)

    user = db.relationship('User', foreign_keys='UserDislike.user_id', overlaps="user_dislikes,user_dislikes")
    dislike_choices = db.relationship('DislikeChoice', foreign_keys='UserDislike.dislike_id',
                                      overlaps="dislike_choices_id,user_dislikes")

    def __str__(self):
        return self.label

# ---------------------------------------------------------------------------------------------------------------------

