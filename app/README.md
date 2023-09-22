_I have almost definitely made some mistakes while doing this haha, so please do not hesitate to point them out / fix them when you inevitably spot them_

---
1. To run the flask app : 
-
To make sure that your environment is set up correctly for our app to run, please follow these instructions:

Make sure that you have got a virtual environment activated - I think that sometimes pycharm asks you if you want to activate an environment? If so, say yes.

Otherwise, to get into a virtual environment: in the terminal, make sure that you are in the project-for-CFG folder, and then type these commands (one at a time):

$ python -m venv venv
$ source venv/bin/activate

_Please make sure you have installed all the necessary libraries - by running the following command_:
$ pip install -r requirements.txt

Then to run the app, run the following command:
$ flask --app app run     

_OR_

- **flask --app app run --debug**

_OR_

- **flask run**

In the terminal, a link will then appear that looks like this :
 * Running on http://127.0.0.1:5000

2. Click that link, and our apps homepage will open in a new window in your browser! 

_Remember : for the app to work, you have to be running the above code in your Pycharm terminal. If you eg. close Pycharm, or close the 
terminal window, it will stop working in your browser._ 

3. You can then navigate to the different pages in our app, by adding their routes (below) to the end of the address 

_These are the routes that are currently functional / have something to look at :_

- The login page - /login
- The signup page - /signup
- The story page - /ai_story
- The home page - /


So your address bar will have : http://127.0.0.1:5000/

And to eg. navigate to the signup page the address bar should read : **127.0.0.1:5000/signup**

---
**Workflow**
-
**I know it's a bit annoying to remember. So I thought I would outline the workflow steps for completing a task :**
1. Create a branch for your specific task, eg : **ellen-rewrite-readme**

_You can either create this in GitHub, or in Pycharm using the built-in Git features (or the terminal)_
2. Make sure you are using / that you have checked out the branch. If you aren't sure you can write **git status** in
the terminal


3. Do your task :)

_Please tread very lightly when it comes to the init.py file, the routes and the database initialisation. They are very easy to break haha_


4. If it has been a while since you created your branch, and in the meantime changes have been made to then main repo,
before you commit please : 

- **git stash** - this will stash all your new changes, so you don't lose them
- **git pull** - this will pull all the new changes from the main repo, so your version is up to date
- **git stash pop** - this will put all your new changes back

5. Check the app is still working properly - run the flask app and navigate to every page, to make sure it isn't throwing any errors

_Later down the line, we will hopefully also have tests to run_


6. Do your commit and push to **your branch**. I'm sure you know these steps, but just in case :

- **git status** - to check 100% you are on your branch
- _add any files you have edited using **git add <filename.py>**_
- **git commit -m "<add a comment about what you've changed>"**
- **git push**

7. Make a pull request on GitHub, adding us all as reviewers


8. Once we've reviewed it you can review any comments etc, then click to merge with the main codebase when you're happy


9. GitHub will then prompt you to delete your branch, and, as we say in Barnsley, "jobs a good'un!"

---
**App General Info, as requested** 
-
I will leave the outline for each folder / file below, but just to give an overview :

The app directory is broken up into four sections : static, templates, tests and then everything else (more details
about all of these below). 

It has also been broken up into files for each specific purpose - eg. forms.py, for the forms. So that 
each of us can be working on a different file for our specific tasks at the same time and still merge without 
any issues, because we won't need to make significant changes to the same code.

The init.py file has the code that tells the app to run. It also has all the key functionality from all the other files imported 
into it, and that's what ties the app together as a whole.  _So, if you build any major functionality, you may have to 
import it to the init file_. 


Essentially, the app works because the user is routed to a frontend template for each page of our app. These pages then
contain different functionality. Both the route, and the functionality is imported into init.py from elsewhere in the 
codebase (eg. the routes coming from routes.py). The route then shows them the specific .html template for that page. 






### Other Info : 

- The code to refer to the database is : **db = SQLAlchemy()**

_if you have syntax that has **db** anywhere, you will more than likely need that at the top of the file_

- Inside the 'everything else' portion of the app directory, the app can be referred to as **__ name __** 


- Elsewhere, such as in the test files, you may need to import it : 
**from app import app**

Note : 
Please make sure you only import app, or the different pages functionality eg. the routes blueprint, if you need to.
Otherwise, it breaks the entire thing (which I learnt the hard way haha). _If you are getting an error code about a 'circular import', this is why!_ 


---
_There is more specific information about what is to be included at the top of each page, but here is a rundown of what is in each folder / file :_ 

**Static folder**
-
Contains any 'static' elements to our webapp eg. CSS, images etc. Also has a folder for any JavaScript we may need for
the frontend.

**Templates folder**
-
Contains the .html frontend files, to be shown to the end user when they navigate to different pages inside the webapp. 

These are each routed to in the routes.py file - _if you make a new route please make sure it is either routed to one of 
these, or that you make a new one, otherwise it will throw an error_

They contain boilerplate HTML for now, which we can edit to be fancier if we have time / the inclination

- 404.html : contains the custom error page, for if a user navigates to a page on the app that doesn't exist - _this is not currently working_
- ai_story.html : is the page that generates / displays the story
- base.html : contains some functional bootstrap code that katy wrote 
- home.html : contains the homepage
- login.html : contains the login page
- routine.html : will contain the form for choosing a bedtime routine / generating a random one
- signup.html : contains the form for singing up a new user

_note : story.html was the original file for the story generation page, and it hasn't been deleted yet_

**Tests Folder**
-
- __init__.py : contains the test initialisations, and imports the test modules from the files below. 

_I have also imported pytest for the additional functionality, and added a sample test_that you can copy, paste and edit.
- test_openai.py : will contain the tests for the openai page functionality 
- test_routines.py : will contain the tests for the routines page functionality

_As new parts of the app are created, new test files should also be created and their modules imported into the tests>init.py file.


_If we all create tests as we go along, we will end up with a better product overall, and it will also make the job much easier 
for Lauren (who is assigned the testing big ticket)_

**The Rest**
-

- __init__.py : the main code file - contains the app object (__name__) to be used elsewhere in the app
- config.py : configuration variables for the app
- forms.py : the forms for creating a new user (done), and for selecting a bedtime routine
- models.py : database model definitions and methods, as well as code to validate the data before it is put in the database*
- openai.py : code for the functionality of the stories generated using the ai API
- requirements.txt : a list of libraries needed to use the app
- routes.py : the routes that map to the html pages above, telling the app what to show the user on each page. 

These have all been made with and combined into the **routes_bp** variable you can see defined at the top. This is the 
'routes blueprint' - it allows us to import all the routes into the init.py file en masse, as well as giving us some extra 
functionality. 

Because of this, to make a new route we can just define it using the **@routes_bp.route** decorator _(copy the syntax 
from the existing ones and edit, if you are unsure)_, and we don't have to do anything else!

- routines.py : the functions for generating the prompts that make the kids do their routines 

*I have read that apparently you can do this right in the route (katy also did a similar thing for the signup page)
so we might not need this file at all. But I will leave that to the database people to decide.
