""" This page contains tests for the openai page
I wrote these very quickly, and I am not sure that they function correctly - Ellen """

import pytest
import openai
from app.openai import Story, Popup

openai.api_key = "dSiFzoAtYGsmHSyJmEuTT3BlbkFJixDlsmA0rZPOxOfStk6t"


# tests whether the story functions using valid input :
class TestStoryValid:
    @pytest.fixture
    def story_instance(self):
        kind_of_story = "Adventure"
        name = "Alex"
        creature = "dragon"
        pronouns = "they"
        age = 7
        dislikes = "spiders"
        return Story(kind_of_story, name, creature, pronouns, age, dislikes)

    def test_ai_request_output_type(self, story_instance):
        prompt = "Please write the beginning of a story."
        story = Story.ai_request(prompt)
        assert isinstance(story, str)

    def test_generate_story_output_type(self, story_instance):
        story_parts = story_instance.generate_story([])
        assert isinstance(story_parts, list)
        assert all(isinstance(part, str) for part in story_parts)

    def test_generate_story_word_count(self, story_instance):
        story_parts = story_instance.generate_story([])
        total_words = sum(len(part.split()) for part in story_parts)
        assert total_words <= 600

    def test_generate_story_contains_title(self, story_instance):
        story_parts = story_instance.generate_story([])
        assert any("Title" in part for part in story_parts)


# tests for how the story functions with invalid / edge cases - as only can be effected by input, I focus the testing on that
class TestStoryBlank:
    @pytest.fixture
    def story_instance(self):
        kind_of_story = "Adventure"
        name = ""
        creature = "dragon"
        pronouns = "they"
        age = 7
        dislikes = "spiders"
        return Story(kind_of_story, name, creature, pronouns, age, dislikes)

    def test_ai_request_output_type(self, story_instance):
        prompt = "Please write the beginning of a story."
        story = Story.ai_request(prompt)
        assert isinstance(story, str)

    def test_generate_story_output_type(self, story_instance):
        story_parts = story_instance.generate_story([])
        assert isinstance(story_parts, list)
        assert all(isinstance(part, str) for part in story_parts)

    def test_generate_story_word_count(self, story_instance):
        story_parts = story_instance.generate_story([])
        total_words = sum(len(part.split()) for part in story_parts)
        assert total_words <= 600

    def test_generate_story_contains_title(self, story_instance):
        story_parts = story_instance.generate_story([])
        assert any("Title" in part for part in story_parts)

# Tests for if the name input is a number. This shouldn't be the case, we have a regex valadator on the form :
class TestStoryInt:
    @pytest.fixture
    def story_instance(self):
        kind_of_story = "Adventure"
        name = 444444444444444444444444444444444
        creature = "dragon"
        pronouns = "they"
        age = 7
        dislikes = "spiders"
        return Story(kind_of_story, name, creature, pronouns, age, dislikes)

    def test_ai_request_output_type(self, story_instance):
        prompt = "Please write the beginning of a story."
        story = Story.ai_request(prompt)
        assert isinstance(story, str)

    def test_generate_story_output_type(self, story_instance):
        story_parts = story_instance.generate_story([])
        assert isinstance(story_parts, list)
        assert all(isinstance(part, str) for part in story_parts)

    def test_generate_story_word_count(self, story_instance):
        story_parts = story_instance.generate_story([])
        total_words = sum(len(part.split()) for part in story_parts)
        assert total_words <= 600

    def test_generate_story_contains_title(self, story_instance):
        story_parts = story_instance.generate_story([])
        assert any("Title" in part for part in story_parts)


# tests for if the input is a symbol :
class TestStorySymbol:
    @pytest.fixture
    def story_instance(self):
        kind_of_story = "Adventure"
        name = "££££"
        creature = "dragon"
        pronouns = "they"
        age = 7
        dislikes = "spiders"
        return Story(kind_of_story, name, creature, pronouns, age, dislikes)

    def test_ai_request_output_type(self, story_instance):
        prompt = "Please write the beginning of a story."
        story = Story.ai_request(prompt)
        assert isinstance(story, str)

    def test_generate_story_output_type(self, story_instance):
        story_parts = story_instance.generate_story([])
        assert isinstance(story_parts, list)
        assert all(isinstance(part, str) for part in story_parts)

    def test_generate_story_word_count(self, story_instance):
        story_parts = story_instance.generate_story([])
        total_words = sum(len(part.split()) for part in story_parts)
        assert total_words <= 600

    def test_generate_story_contains_title(self, story_instance):
        story_parts = story_instance.generate_story([])
        assert any("Title" in part for part in story_parts)


# tests for a long name string :
class TestStoryLong:
    @pytest.fixture
    def story_instance(self):
        kind_of_story = "Adventure"
        name = "this is not a name this is a very long string this is not a name this is a very long string this is not a name this is a very long string this is not a name this is a very long string "
        creature = "dragon"
        pronouns = "they"
        age = 7
        dislikes = "spiders"
        return Story(kind_of_story, name, creature, pronouns, age, dislikes)

    def test_ai_request_output_type(self, story_instance):
        prompt = "Please write the beginning of a story."
        story = Story.ai_request(prompt)
        assert isinstance(story, str)

    def test_generate_story_output_type(self, story_instance):
        story_parts = story_instance.generate_story([])
        assert isinstance(story_parts, list)
        assert all(isinstance(part, str) for part in story_parts)

    def test_generate_story_word_count(self, story_instance):
        story_parts = story_instance.generate_story([])
        total_words = sum(len(part.split()) for part in story_parts)
        assert total_words <= 600

    def test_generate_story_contains_title(self, story_instance):
        story_parts = story_instance.generate_story([])
        assert any("Title" in part for part in story_parts)


# tests for a short name string
class TestStoryShort:
    @pytest.fixture
    def story_instance(self):
        kind_of_story = "Adventure"
        name = "a"
        creature = "dragon"
        pronouns = "they"
        age = 7
        dislikes = "spiders"
        return Story(kind_of_story, name, creature, pronouns, age, dislikes)

    def test_ai_request_output_type(self, story_instance):
        prompt = "Please write the beginning of a story."
        story = Story.ai_request(prompt)
        assert isinstance(story, str)

    def test_generate_story_output_type(self, story_instance):
        story_parts = story_instance.generate_story([])
        assert isinstance(story_parts, list)
        assert all(isinstance(part, str) for part in story_parts)

    def test_generate_story_word_count(self, story_instance):
        story_parts = story_instance.generate_story([])
        total_words = sum(len(part.split()) for part in story_parts)
        assert total_words <= 600

    def test_generate_story_contains_title(self, story_instance):
        story_parts = story_instance.generate_story([])
        assert any("Title" in part for part in story_parts)

# TESTS FOR THE POPUPS -------------------------------------------------------------------------------------------------
# test a popup with valid input
class TestPopupValid:
    @pytest.fixture
    def popup_instance(self):
        name = "Alex"
        step = "Brush teeth"
        story = "Once upon a time, there was a brave adventurer."
        return Popup(name, step, story)

    def test_ai_request_output_type(self, popup_instance):
        prompt = popup_instance.popup_prompt()
        popup_text = Popup.ai_request(prompt)
        assert isinstance(popup_text, str)

    def test_generate_popups_output_type(self, popup_instance):
        popup_text = popup_instance.generate_popups([])
        assert isinstance(popup_text, list)
        assert all(isinstance(popup, str) for popup in popup_text)

    def test_generate_popups_word_count(self, popup_instance):
        popup_text = popup_instance.generate_popups([])
        total_words = sum(len(popup.split()) for popup in popup_text)
        assert total_words <= 50

    def test_generate_popups_contains_bedtime_steps(self, popup_instance):
        bedtime_steps = ["Brush teeth", "Brush hair", "Take vitamins", "Turn on nightlight", "Turn off light"]
        popup_text = popup_instance.generate_popups([])
        assert all(step in popup for step in bedtime_steps for popup in popup_text)


# test a popup with invalid / edge inputs :
class TestPopupBlank:
    @pytest.fixture
    def popup_instance(self):
        name = ""
        step = "Brush teeth"
        story = "Once upon a time, there was a brave adventurer."
        return Popup(name, step, story)

    def test_ai_request_output_type(self, popup_instance):
        prompt = "Please write a pop-up text."
        popup_text = Popup.ai_request(prompt)
        assert isinstance(popup_text, str)

    def test_generate_popups_output_type(self, popup_instance):
        popup_text = popup_instance.generate_popups([])
        assert isinstance(popup_text, list)
        assert all(isinstance(popup, str) for popup in popup_text)

    def test_generate_popups_word_count(self, popup_instance):
        popup_text = popup_instance.generate_popups([])
        total_words = sum(len(popup.split()) for popup in popup_text)
        assert total_words <= 50

    def test_generate_popups_contains_bedtime_steps(self, popup_instance):
        bedtime_steps = ["Brush teeth", "Brush hair", "Take vitamins", "Turn on nightlight", "Turn off light"]
        popup_text = popup_instance.generate_popups([])
        assert all(step in popup for step in bedtime_steps for popup in popup_text)


# TESTS FOR APPROPRIATENESS .. NOT FINISHED : --------------------------------------------------------------------------

# class TestAppropriateness:
#     @pytest.fixture
#     def story_instance(self):
#         kind_of_story = "Adventure"
#         name = "Alex"
#         creature = "dragon"
#         pronouns = "they"
#         age = 7
#         dislikes = "spiders"
#         return Story(kind_of_story, name, creature, pronouns, age, dislikes)
#
#     def test_check_appropriateness_for_children(self):
#         # Example test for checking appropriateness for children
#         story = "Once upon a time, there was a friendly unicorn."
#         popup = "Brush your teeth and get ready for bed."
#
#         # Call appropriateness checking function or library
#         is_story_appropriate = check_appropriateness_for_children(story)
#         is_popup_appropriate = check_appropriateness_for_children(popup)
#
#         # Assert that the story is appropriate for children
#         assert is_story_appropriate
#
#         # Assert that the popup is appropriate for children
#         assert is_popup_appropriate
#
#
# def check_appropriateness_for_children(content):
#     # need
#     return True

