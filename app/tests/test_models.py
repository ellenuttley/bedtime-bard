'''This page should contain tests for the models page, not currently functional'''
#
# import pytest
#
# from ..models import User, BedtimeSteps, CreatureChoice, StoryTypeChoice,DislikeChoice, UserCreature, UserStoryType, UserDislike, UserBedtimeRoutine
#
# def test_new_user():
#     """
#     GIVEN a User model
#     WHEN a new User is created
#     THEN check the username, and hashed_password fields are defined correctly
#     *password given is not being hashed therefore test is failing.
#     """
#     user = User(username='ellen_uttley', password='test-password')
#     assert user.username == 'ellen_uttley'
#     assert user.password != 'test-password'
#
# # This test is not being run for some reason
# def test_bedtime_steps():
#     steps = BedtimeSteps(id=1, label='Brush Teeth')
#     assert steps.id == 1
#     assert steps.label == 'Brush Teeth'
#
#
# def test_creature_choices():
#     choices = CreatureChoice(id=1, label='dragon')
#     assert choices.id == 1
#     assert choices.label == 'dragon'
#
#
# def test_story_type_choice():
#     storychoice = StoryTypeChoice(id=1, label='happy stories')
#     assert storychoice.id == 1
#     assert storychoice.label == 'happy stories'
#
#
# def test_dislike_choice():
#     dislike = DislikeChoice(id=1, label='mystery stories')
#     assert dislike.id == 1
#     assert dislike.label == 'mystery stories'
#
#
# def test_user_creature():
#     creature = UserCreature(id=1, user_id=1, creature_id=1)
#     assert creature.id == 1
#     assert creature.user_id == 1
#     assert creature.creature_id == 1
#
#
# def test_user_story_type():
#     storyType = UserStoryType(id=1, user_id=1, story_type_id=1)
#     assert storyType.id == 1
#     assert storyType.user_id == 1
#     assert storyType.story_type_id == 1
#
#
# def test_user_dislike():
#     dislike = UserDislike(id=1, user_id=1, dislike_id=1)
#     assert dislike.id == 1
#     assert dislike.user_id == 1
#     assert dislike.dislike_id == 1
#
#
# def test_user_bedtime_routine():
#     routine = UserBedtimeRoutine(id=1, user_id=1, bedtime_step_id=1, position=1)
#     assert routine.id == 1
#     assert routine.user_id == 1
#     assert routine.bedtime_step_id == 1
#     assert routine.position == 1
#
# # class test_all_routes(pytest):
#
# #     def test_new_user():
# #         user = User('ellen_uttley', 'test-password')
# #         self.assert user.id == 'ellen_uttley'
# #         self.assert user.password != 'test-password'
# #         self.assert user.role == 'user'
#
# #     def test_bedtime_steps(self):
# #         steps = BedtimeSteps(1, 'example') #update with correct example
# #         self.assert steps.id == 1
# #         self.assert steps.label == 'example'
#
#
#
# #     def test_creature_choices(self):
# #         choices = CreatureChoice(1, 'dragon')
# #         self.assert choices.id == 1
# #         self.assert choices.label == 'dragon'
#
#
# #     def test_story_type_choice(self):
# #         storychoice = StoryTypeChoice(1, 'happy stories')
# #         self.assert storychoice.id == 1
# #         self.assert storychoice.label == 'happy stories'
#
#
# #     def test_dislike_choice(self):
# #         dislike = DislikeChoice(1, 'mystery stories')
# #         self.assert dislike.id == 1
# #         self.assert dislike.label == 'mystery stories'
#
#
# #     def test_user_creature(self):
# #         creature = UserCreature(1, 1, 'tiger')
# #         self.assert creature.id == 1
# #         self.assert creature.user_id == 1
# #         self.assert creature.label == 'tiger'
#
#
# #     def test_user_story_type(self):
# #         storyType = UserStoryType(1, 1, 'happy stories')
# #         self.assert storyType.id == 1
# #         self.assert storyType.user_id == 1
# #         self.assert storyType.label == 'happy stories'
#
#
# #     def test_user_dislike(self):
# #         dislike = UserDislike(1, 1, 'happy stories')
# #         self.assert dislike.id == 1
# #         self.assert dislike.user_id == 1
# #         self.assert dislike.label == 'happy stories'
#
#
# #     def test_user_bedtime_routine(self):
# #         routine = UserBedtimeRoutine(1, 1, 1, 1)
# #         self.assert routine.id == 1
# #         self.assert routine.user_id == 1
# #         self.assert routine.bedtime_step_id == 1
# #         self.assert routine.position == 1
#
#
# if __name__ == '__main__':
#     pytest.main()
#
