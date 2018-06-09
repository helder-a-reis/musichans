# Musichans
Following instructions are to create a development environment for Musichans on a Windows machine.

## Pre requirements
- Conda (https://conda.io/docs/index.html) for creating and managing virtual environments (Python will be installed automatically)
- A Python IDE (I use Eclipse with PyDev http://www.pydev.org/)

## Configuration
### Conda
A Conda environment file is included. Open "Anaconda command prompt", navigate to your project folder and run
- conda env create -f musichans.yml 

Activate the environment
- activate musichans

see https://conda.io/docs/user-guide/tasks/manage-environments.html#creating-an-environment-from-an-environment-yml-file for more info.

### Eclipse
Open the project. Go to Properties->PyDev-Intepreter/Grammar, "Click here to configure an interpreter not listed", "New", navigate to the environment executable, example "D:\Anaconda3\envs\musichans\python.exe", set Interpreter to "musichans", OK, OK, select musichans as the Interpreter, "Apply and Close". This will find all the projects dependencies and run it under the musichans virtual environment.
PyDev is recommended for working with Python in Eclipse. It also supports Django, see http://www.pydev.org/manual_adv_django.html .

There's also a GitHub plugin for Eclipse, very useful. After installing it, right click on the project root, select, them "Commit" or "Pull", etc.

### PyCharm
Good luck. (it's supposed to work really nicely, although Django is only supported in the Pro version)

### Database
For development we are using SQLite, so no additional configuration needed.

### Webserver
For development we're using the WSGI provided by Django

## File structure
Django has already created the basic structure, it's all in the musichans folder. 

## Starting the website
Open Anaconda prompt, navigate inside the musichans site (where manage.py is), run
- python manage.py runserver

## Applications
Description of the applications in the project is below. See https://docs.djangoproject.com/en/2.0/ref/applications/#projects-and-applications for diference between Projects and Applications:
- members: everything related to a site user: sign up, manage profile, etc. Didn't call it "musicians" as it's too similar to the site name and causes confusion.
- bands (to be created): everything related to bands and their profiles
- music (to be created): generic music info such as instruments played, roles in a band, genres, groups, etc, to be used in bands and members
- posts (to be created): posts searching for musicians, annoncing concerts, etc. Was going to call it ads but could be confusion with the comercial ads later.