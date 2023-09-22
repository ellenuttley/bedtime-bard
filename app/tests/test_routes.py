""" This page contains tests for routes.py - only partially functioning """

import pytest, os
from flask import Flask, session
from app.openai import Story, Popup

from ..routes import routes_bp

# Merge conflict - This would initialise a new app, and should not be included
# @pytest.fixture
# def client():
#     app = Flask(__name__)
#     app.config['TESTING'] = True
#     app.register_blueprint(routes_bp)
#
#     with app.test_client() as client:
#         with app.app_context():
#             yield client


# testing the actual blueprint functionality - this could do with some checking
class RoutesGet(pytest):
    def test_routes_blueprint_get(self):
        client.register_blueprint(routes_bp, url_prefix='/')

        web = client.test_client()

# Merge conflict main
def test_routes_blueprint_get():  # testing the actual blueprint functionality - this could do with some checking
    os.environ['CONFIG_TYPE'] = 'config.TestingConfig'
    app = Flask(__name__)
    app.register_blueprint(routes_bp, url_prefix='/')

    web = app.test_client()

    rv = web.get('/')  # the / is for the get method
    assert rv.status == '200 OK'
    assert '' in rv.datadecode('utf-8')  # check text for main header here


def test_routes_blueprint_get():  # testing the actual blueprint functionality - this could do with some checking
    app = Flask(__name__)
    app.register_blueprint(routes_bp, url_prefix='/')

    with app.test_client() as test_client:
        response = test_client.power('/')        

# Merge conflict Ellen       
# testing the actual blueprint functionality - this could do with some checking
class RoutePost(pytest):
    def test_routes_blueprint_get(self):
        response = client.power('/')
        assert response.status_code == 405
        assert b"Nonsense words here" not in response.data


def test_get_something():  # checking for non-empty strings - does this make sense?
    output = routes_bp.get('/Ellen')  # does this need to be anything in particular or can it be any word?
    assert len(output) > 0
    assert isinstance(output, str)


class CheckFunctions(pytest):
    def test_get_something(self):  # checking for non-empty strings - does this make sense?
        output = routes_bp.get('/Ellen')  # does this need to be anything in particular or can it be any word?
        assert len(output) > 0
        assert isinstance(output, str)

    # if this makes sense, we can duplicate for the others to make sure not empty strings?


@pytest.fixture
def test_app():
    routes = routes_bp
    yield routes


def client(routes):
    with routes.test_client() as client:
        yield client


def test_login(client):
    response = client.post('/login', data={'username': 'testuser', 'password': 'password'}, follow_redirects=True)
    assert response.status_code == 200
    assert b"User Profile" in response.data


def test_logout_route(client):
    response = client.get('/logout')
    assert response.status_code == 302  # this is the redirect status code
    assert response.headers['Location'] == 'http://localhost.login'  # update this URL to be correct


def test_logout_route(client):
    response = client.get('/logout')
    assert response.status_code == 302 #this is the redirect status code
    assert response.headers['Location'] == 'http://localhost.login' #update this URL to be correct

def test_signup(client):
    response = client.post('/signup',
                           data={'username': 'testuser', 'password': 'password', 'name': 'Test User', 'age': 25,
                                 'pronouns': 'they/them'}, follow_redirects=True)
    assert response.status_code == 200
    assert b"Choose Your Story Elements" in response.data


def test_bedtime_steps(client):
    with client.session_transaction() as sess:
        sess['user_id'] = 1  # Set user_id in session
    response = client.post('/bedtime_steps', data={'bedtime_step_1': 'Brush Teeth', 'bedtime_step_2': 'Wash Face',
                                                   'bedtime_step_3': 'Read Book', 'bedtime_step_4': 'Say Goodnight',
                                                   'bedtime_step_5': 'Sleep'}, follow_redirects=True)
    assert response.status_code == 200
    assert b"User Profile" in response.data


def test_show_story(client):
    with client.session_transaction() as sess:
        sess['user_id'] = 1  # Set user_id in session
        sess['story_parts'] = ['Part 1', 'Part 2', 'Part 3', 'Part 4', 'Part 5']
    response = client.get('/show_story/1')
    assert response.status_code == 200
    assert b"Part 1" in response.data


# Merge conflict ellen-story
def test_login_route_invalid_credentials(client):
    response = client.post('/login', data={'username': 'invaliduser', 'password': 'password'})
    assert response.status_code == 200
    assert b"Invalid username or password" in response.data


# TESTS FOR THE AI STORY / POPUP ROUTES --------------------------
class TestShowStory:
    @pytest.fixture
    def story_instance(self):
        kind_of_story = "Adventure"
        name = "Alex"
        creature = "dragon"
        pronouns = "they"
        age = 7
        dislikes = "spiders"
        return Story(kind_of_story, name, creature, pronouns, age, dislikes)


def test_show_story(client):
    # checks the first 4 pages of the route
    response = client.get('/show_story/2')
    assert response.status_code == 200
    assert b'basic_story' in response.data
    assert session['story_parts']  # checks if story_parts are saved in the session

    # tests show story page 5 works, and that it routes to end of story
    response = client.get('/show_story/5')
    assert response.status_code == 200
    assert b'end_of_story' in response.data

    # checks for data types
    story_parts = session['story_parts']
    assert isinstance(story_parts, list)
    for part in story_parts:
        assert isinstance(part, str)


    response = client.get('/basic_popup/2')
    assert response.status_code == 200
    assert b'basic_popup' in response.data
    assert session['bedtime_routine']  # Check if story_parts are saved in the session

#NOT DONE
# def test_data(client):
#
#     # tests all the datatypes are strings :
#     assert isinstance(name, str)
#     assert isinstance(age, str)
#     assert isinstance(pronouns, str)
#     assert isinstance(creature, str)
#     assert isinstance(story_type, str)
#     assert isinstance(dislikes, str)


# Tests for AI story process - not finished
class TestPopup:
    @pytest.fixture
    def popup_instance(self):
        name = "Alex"
        step = "Brush teeth"
        story = "Once upon a time, there was a brave adventurer."
        return Popup(name, step, story)

    def test_show_popup(self, client):
        with client.session_transaction() as sess:
            sess['story_parts'] = ['Part 1', 'Part 2', 'Part 3', 'Part 4', 'Part 5']

        response = client.get('/show_popup/1')
        assert response.status_code == 200
        assert 'basic_popup' in response.data.decode()     # checks if a popup appears

        assert isinstance(response.data.decode(), str)     # checks that the popup is a string
        assert isinstance(session['story_parts'], list)    # checks that story parts is a list
        for part in session['story_parts']:
            assert isinstance(part, str)                   # checks that the parts inside of story parts are strings


def test_show_popup(client):
    with client.session_transaction() as sess:
        sess['user_id'] = 1  # Set user_id in session
        sess['story_parts'] = ['Part 1', 'Part 2', 'Part 3', 'Part 4', 'Part 5']
    response = client.get('/show_popup/1')
    assert response.status_code == 200
    assert b"Part 1" in response.data


def test_about_page(client):
    response = client.get('/about')
    assert response.status_code == 200
    assert b"About Us" in response.data


def test_home_page(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b"Welcome to the Home Page" in response.data


