"""
This file contains the various OOP pieces for the operation of the story generation algorithm.
The story generation process weaves in and out of here, and I have tried to note the process well to make it as easy to
follow as possible.
"""
import openai

# Story Generation Step : 2 -- Full generation process in story_generation route in routes.py -------------------------
# Creates a Story instance, with all the elements needed to inform the prompt
class Story:
    def __init__(self, name, age, pronouns, story_type, creature, dislikes):
        self.name = name
        self.age = age
        self.pronouns = pronouns
        self.story_type = story_type
        self.creature = creature
        self.dislikes = dislikes

# ---------------------------------------------------------------------------------------------------------------------

    # Method to send the AI request via the API
    # The prompts are generated via the _prompt methods below
    @staticmethod
    def ai_request(prompt):
        global story    
        try:            # Exception handling for the moderation - to check whether the story passes the check
            response = openai.Completion.create(
                model="text-davinci-003",
                prompt=prompt,
                temperature=0.7,
                max_tokens=1024,
                top_p=1.0,
                frequency_penalty=0.5,
                presence_penalty=0.0

            )
            story = response.choices[0].text.strip()
            openai.Moderation.create(input=story)
        except openai.Moderation.result.flagged:  # If it is flagged, then the process starts again with the same prompt
            Story.ai_request(prompt)
        finally:
            return story

    # Writes the prompt for the opening part of the story, using the variables in the story object
    # ... that prompt is then passed to the ai_request method above.
    def opening_prompt(self):
        prompt = f"""Please write the beginning of a {self.story_type} story about a child who uses {self.pronouns}
        named {self.name} and a {self.creature}. The story should be appropriate for {self.age} year olds, and the child
        this story is for does not like {self.dislikes}. The content of the story should not be effected by the child's
        name or gender. This set up should be less than 200 words, and should end on a cliffhanger.
        Please give the story a title"""
        return prompt

    # Writes the prompts for all the subsequent parts of the story

    def story_part_prompt(self, story, story_part):
        prompt = f"""Please continue writing this story: {story}. The next part of the story should be the
        {story_part}, and should smoothly carry on from the previous part. The story should be appropriate for {self.age}
        aged children, and the content should not be effected by the child's name or gender. This part of the story
        should be less than 200 words, and should end with a cliffhanger."""
        return prompt

# Story Generation Step : 3 -- Full generation process in story_generation route in routes.py -------------------------
    # Method to generate the story, utilising the other methods above
    # The story_pieces argument is the story content so far, so when this method is called in routes this list contains
    # only the story opening, and it is then added to with each loop.
    def generate_story(self, story_pieces=[]):
        story_parts = ["inciting incident", "rising action", "all-is-lost moment", "happy ending"]  # story arc

        prompt = self.opening_prompt()                           
        story = ""                                               
        story += self.ai_request(prompt)                         
        story_pieces.append(self.ai_request(prompt))             
        for i in story_parts:                                    
            next_prompt = self.story_part_prompt(story, i)      
            story_pieces.append(self.ai_request(next_prompt))    
            story += self.ai_request(next_prompt)               
        return story_pieces                                      
                                                                 


# Story Generation Step : 4 -- Full generation process in story_generation route in routes.py--------------------------
    # Creates a Popup instance, with all the elements needed to inform the prompt
    # The popup objects contain the child / current users name (or names, in the case of sibling groups)
    # ... the current routine bedtime step, and the story so far.
class Popup:
    def __init__(self, name, step, story):
        self.name = name
        self.step = step
        self.story = story

# ---------------------------------------------------------------------------------------------------------------------

    # Method to send the AI request via the API
    # The prompts are generated via the _prompt methods below
    @staticmethod
    def ai_request(prompt):
        global popup_text      # Allows popup_text to be accessed elsewhere, I am not sure if it is working as intended
        try:
            response = openai.Completion.create(
                model="text-davinci-003",
                prompt=prompt,
                temperature=0.7,
                max_tokens=1024,
                # n=1,
                top_p=1.0,
                # stop=None,
                frequency_penalty=0.5,
                presence_penalty=0.0

            )
            popup_text = response.choices[0].text.strip()
            openai.Moderation.create(input=popup_text)
        except openai.Moderation.result.flagged:               # if it is flagged, then make a different popup :
            Popup.ai_request(prompt)
        finally:
            return popup_text

    # Method to write the prompt for each popup, that prompt is then passed to the ai_request method above.
    # Each prompt / popup will contain one bedtime step
    # It incorporates what is happening in the current part of the story, and also asks for a sense of urgency - to
    # encourage the child to not dawdle through their step.
    def popup_prompt(self):
        prompt = f"""Please write the text for a pop-up, to encourage a child called {self.name} to {self.step}
        it should be related to this story {self.story}, less than 20 words, and have a sense of urgency"""
        return prompt

# Story Generation Step : 5 -- Full generation process in story_generation route in routes.py -------------------------
    # Method to generate the popup text, utilising the other methods defined above.
    # The pop_ups argument is the list of the popup objects generated in the story generation route
    @staticmethod
    def generate_popups(pop_ups, popup_text=[]):
        # uses the list of popups to generate individual prompts for each
        popup_prompts = [pop_ups[0].popup_prompt(), pop_ups[1].popup_prompt(), pop_ups[2].popup_prompt(),
                         pop_ups[3].popup_prompt(), pop_ups[4].popup_prompt()]
        # then uses these prompts to generate the popup content via API request
        popup_requests = [pop_ups[0].ai_request(popup_prompts[0]), pop_ups[1].ai_request(popup_prompts[1]),
                          pop_ups[2].ai_request(popup_prompts[2]), pop_ups[3].ai_request(popup_prompts[3]),
                          pop_ups[4].ai_request(popup_prompts[4])]
        for ai_request in popup_requests:
            popup_text.append(ai_request)       # all the individual popups content are then saved to a list
        return popup_text                       # and then returned, to be shown on the appropriate show_popup page

# ---------------------------------------------------------------------------------------------------------------------

