![image](https://github.com/catrionafsmith/project-for-CFG/assets/113264368/b7384985-1a19-4f26-8d8a-3ac933379d3f)
Bedtime can be a challenging and frustrating daily experience for children and parents. To address this, we have developed an AI-powered webapp that generates tailored-made stories, that encourage a child through the bedtime transition in a smoothe, engaging and enjoyable way - for everyone!

Utilising artificial intelligence via the OpenAI API, the app will generate a unique story every night; capturing the child's imagination and incorporating their interests to maximise their enjoyment, while prompting children to perform the pre-selected bedtime steps via pop-ups throughout the story. These prompts are tailored to the story, and transform the routine into an exciting adventure, encouraging the child to complete their bedtime task, and ending with them tucked up in bed.

## How to Use 🛠️
_**Note :** before running for the first time, please go into \_init\_.py and un-comment line 53_

Once you have cloned the repo - make sure that you are in the `app` folder, and then type these commands into the terminal (one at a time) :  
>`python -m venv venv`
  
>`.\\venv\\Scripts\\activate`
  
_or : `source venv/bin/activate` for Mac / Linux_  
  
>` cd ../`
  
>`pip install -r requirements.txt`

_Finally,  to run the app :_ 
>`flask --app app run`
  
_or : `flask --app app run --debug` to run in debug mode_

In the terminal, a link will then appear that looks like this :  
>`Running on http://127.0.0.1:5000`
  
**_Note : at this point please go into \_init\_.py and re-comment line 53_**  
Click that link, and our apps homepage will open in a new window in your browser! 

## The UX Design 🎨
![Copy of  Bedtime Bard Wireframe Designs  User Story](https://github.com/ellenuttley/bedtime-bard/assets/113264368/597769bd-f735-47dd-b2c0-9a04ba4d3a4f)

## Languages, Frameworks & Libraries Used 🖥️

* Flask
* Python
* SQLAlchemy
* OpenAI
* HTML and CSS

## File Structure 📂

- **Static folder**     : 'static' elements eg. CSS, images etc
- **Templates folder**  : .html frontend files, routed to in the routes.py file
- **Tests Folder**      : contains tests initialisation, and unit tests for each page    _incomplete_
- **__init__.py**       : the main code file - contains the app object (__name__) to be used elsewhere in the app
- **forms.py**          : the forms for creating a new user (done), and for selecting a bedtime routine
- **models.py**         : database model definitions and methods
- **openai.py**         : code for the functionality of the stories generated using the OpenAI API
- **requirements.txt**  : a list of libraries needed to use the app
- **routes.py**         : the routes that map to the html pages above
