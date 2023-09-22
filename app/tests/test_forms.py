'''This page should contain tests for the forms page, not currently functional'''

# import pytest
# from flask import Flask
# from flask_wtf.csrf import CSRFProtect
# from ..forms import NewUserForm, ChooseStoryElements, BedtimeRoutineForm
#
# @pytest.fixture
# def app():
#     app = Flask(__name__)
#     #app.config['SECRET_KEY'] = 'test_secret_key'
#     CSRFProtect(app)
#     return app
#
# class testforms(pytest):
#
#    def test_new_user_form(app):
#     with app.test_request_context():
#         form = NewUserForm(username='test_user', password='test_password', name="John", age=5, pronouns='he/him')
#         assert form.validate() == True
#
#    def test_new_user_form_invalid(app):
#     with app.test_request_context():
#         form = NewUserForm(username='', password='', name='', age='', pronouns='')
#         assert form.validate() == False
#
#    def test_choose_story_elements(app):
#     with app.test_request_context():
#         form = ChooseStoryElements(creature=[1, 2], story_type=[1], dislikes=[2])
#         assert form.validate() == True
#
#    def test_choose_story_elements_invalid(app):
#     with app.test_request_context():
#         form = ChooseStoryElements(creature=[], story_type=[], dislikes=[])
#         assert form.validate() == False
#
#    def test_bedtime_routine_form(app):
#     with app.test_request_context():
#         form = BedtimeRoutineForm(step1=1, step2=2, step3=3, step4=4, step5=5)
#         assert form.validate() == True
#
#    def test_bedtime_routine_form_invalid(app):
#     with app.test_request_context():
#         form = BedtimeRoutineForm(step1='', step2='', step3='', step4='', step5='')
#         assert form.validate() == False
#
