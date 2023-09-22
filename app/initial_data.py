"""T
his page contains the function to insert the initial data into the database.

It inserts the choices into the BedtimeSteps, CreatureChoices, StoryTypeChoices and DislikeChoices models
to then be populated as options in the forms in forms.py
"""

from app.models import BedtimeSteps, CreatureChoice, StoryTypeChoice, DislikeChoice

from app import db


def insert_initial_data():
    bedtime_steps = ["Brush Teeth",
                "Wash Face",
        "Wash Hands and Feet",
        "Take Vitamins",
        "Take Medicine",
        "Have a Snack",
        "Have a Drink",
        "Tidy Up",
        "Say Prayers",
        "Put Pyjamas On",
        "Put Nightclothes On",
        "Hug or Kiss Someone Goodnight",
        "Say Goodnight to Someone",
        "Get Into Bed",
        "Put Lotion On",
        "Put Bonnet On",
        "Put Headwrap On",
        "Turn on Night Light",
        "Brush Hair",
        "Style Hair",
        "Get Favourite Toy",
        "Close Curtains or Blinds",
        "Put on Pull-up",
        "Shower",
        "Bath",
        "Use The Bathroom",
        "Turn off the Light",
        "Say Goodnight to the Moon",
        "Tell a funny joke",
        "Snuggle your Teddy",
        "Sing a Silly Song",
        "Tell a Joke",
                     "Take Glasses Off",
                     "Take Hearing Aid Out"
    ]

    creature_choices = [
        "Dragon", "Mermaid", "Unicorn", "Minion", "Ghost", "Witch", "Cyclops",
        "Creeper", "Shark", "Spider", "Tiger", "Alien", "Dinosaur", "Phoenix",
        "Wizard", "Elf", "Orc", "Goblin", "Genie", "Cow Boy", "Super Hero", "Princess",
        "Fairy", "Prince", "Knight", "Santa", "Tooth Fairy", "Easter Bunny", "Pikachu",
        "Kraken", "Hamster", "Cat", "Dog", "Rabbit", "Snake", "Axolotl"

    ]

    story_types = [
        "Happy Stories",
        "Silly Stories",
        "Funny Stories",
        "Exciting Stories",
        "Puzzling Stories",
        "Educational Stories",
        "Calming Stories",
        "Adventure Stories",
        "Video Game Stories",
        "Fantasy Stories",
        "Sci-Fi Stories",
        "Mystery Stories"
    ]

    dislikes = [
        "Scary Stories",
        "Silly Stories",
        "Puzzling Stories",
        "Educational Stories",
        "Gross Stories",
        "Sad Stories",
        "Calming Stories",
        "Adventure Stories",
        "Video Game Stories",
        "Fantasy Stories",
        "Sci-Fi Stories",
        "Mystery Stories"
    ]

    # Insert dislikes into the database
    for dislike_label in dislikes:
        dislike = DislikeChoice(label=dislike_label)
        db.session.add(dislike)

    # Insert story types into the database
    for story_type_label in story_types:
        story_type = StoryTypeChoice(label=story_type_label)
        db.session.add(story_type)

    # Insert bedtime steps into the database
    for step_label in bedtime_steps:
        step = BedtimeSteps(label=step_label)
        db.session.add(step)

    # Insert creature choices into the database
    for creature_label in creature_choices:
        creature = CreatureChoice(label=creature_label)
        db.session.add(creature)

    db.session.commit()


