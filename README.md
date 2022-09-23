# Legendarium - Project Portfolio 4 - Full Stack Toolkit
## by Siobhán Mooney

![Image of the site on various platforms.](/static/images/readme_responsive.jpg)

### [Click here to view the deployed app.](https://legendarium.herokuapp.com/)
### [Click here to view the repository.](https://github.com/Estelindis/legendarium)

# Table of Contents:
1. [About the Project](#about-the-project)
    1. [User Goals](#user-goals)
    2. [Owner Goals](#owner-goals)
2. [Design](#design)
    1. [Wireframes](#wireframes)
    2. [Data Models](#data-models)
3. [Agile Development](#agile-development)
4. [Testing, Bugs, and Fixes](#testing-bugs-and-fixes)
    1. [HTML Validation](#html-validation)
    2. [CSS Validation](#css-validation)
    3. [Python Validation](#python-validation)
    4. [Other Testing](#other-testing)
5. [Future Features](#future-features)
6. [Deployment](#deployment)
    1. [Deploying to Heroku](#deploying-to-heroku)
    2. [Forking the Repository on GitHub](#forking-the-repository-on-github)
    3. [Cloning the Repository on GitHub](#cloning-the-repository-on-github)
7. [Used technologies and credits](#used-technologies-and-credits)
    1. [Languages](#languages)
    2. [Python Libraries](#python-libraries)
    3. [Other Technologies](#other-technologies)
    4. [Credits](#credits)


# About the project
Legendarium is an online story database for characters, places, objects, or anything else a writer can imagine.  

## User Goals
- Easily navigate a readable, accessible website from any platform.
- Read stories without having to register or log in.
- Register to comment on stories and add them to one's library (this site's version of "likes").

## Owner Goals
- Present stories to users in a readable, accessible format.
- Create, update, and delete stories.
- Categorize stories.
- Add images and notes to stories.

# Design
Legendarium was originally imagined as a database for RPG character backstories.  Its initial wireframes reflect this vision, as does the name of its "chargen" app.  However, as development continued, it was reimagined as a database for stories of all kinds.  

In terms of visuals and data, Legendarium is strongly inspired by the Code Institute "I Think Therefore I Blog" Codestar walkthrough project.  Using the lessons shown in that walkthrough to understand the underlying principles, various changes were made to the 

## Wireframes
![Mobile wireframe.](/static/images/mobile_wireframe.png)
![Desktop wireframe.](/static/images/desktop_wireframe.png)

## Data Models
![Data model diagram.](/static/images/data_model_diagram.jpg)

# Agile Development
- [Legendarium's kanban board.](https://github.com/Estelindis/legendarium/projects/1)

# Testing, Bugs, and Fixes

## HTML Validation
![Mobile wireframe.](/static/images/mobile_wireframe.png)
![Desktop wireframe.](/static/images/desktop_wireframe.png)

## CSS Validation
![Mobile wireframe.](/static/images/mobile_wireframe.png)
![Desktop wireframe.](/static/images/desktop_wireframe.png)

## Python Validation
Some standard AUTH_PASSWORD_VALIDATORS lines from settings.py in the "legendarium" app did not pass validation.
On investigating options for validating these lines, I found [a ticket discussing the topic](https://code.djangoproject.com/ticket/28163), which concluded that these lines should be kept as-is, since "fixing" them to work within the 80-character limit has disadvantages.

The following Python files from the "chargen" app were validated via [PEP8 Online](http://pep8online.com/):
admin.py; forms.py; models.py; urls.py; views.py.

### Admin.py

![PEP8 result for admin.py](/static/images/valid_chargen_admin_py.jpg)

### Forms.py

![PEP8 result for admin.py](/static/images/valid_chargen_forms_py.jpg)

### Models.py

![PEP8 result for admin.py](/static/images/valid_chargen_models_py.jpg)

### URLS.py

![PEP8 result for admin.py](/static/images/valid_chargen_urls_py.jpg)

### Views.py

![PEP8 result for admin.py](/static/images/valid_chargen_views_py.jpg)

## Other Testing
![Mobile wireframe.](/static/images/mobile_wireframe.png)
![Desktop wireframe.](/static/images/desktop_wireframe.png)

# Future Features
- Users should be able to create, update, and delete their own stories.
- Users should be able to view a list of stories added to their libraries.
- Users should be able to view stories filtered by category.
- Users should be able to add (and remove) tags for their own stories, so they can categorize their content beyond the limits of the standard admin-controlled categories.
- Admins should be able to carry out all admin activities without having to access the built-in Django admin panel.  In this scenario, admin functions would appear on the front-end when admins are logged in (e.g. an admin viewing a page with comments would have the option to approve comments directly, from that page). 

# Deployment

## Deploying to Heroku

- Log into Heroku (creating an account if needed).
- Click the "New" button from the dashboard, under the header in the top right corner.
- Choose "Create new app."
- Enter your application name, which has to be unique. Then select your region and click "Create App."
- From your project page, click the "Settings" tab and scroll to "Config Vars."
- Enter "PORT" in the KEY input field, then enter "8000" in the VALUE input field.
- Click the "Add" button to add the Convig Vars.
- On the same page, scroll to the buildpacks section and click "Add Buildpack."
- Add the Python and node.js buildpacks, ensuring that the Python buildpack is listed above the node.js buildpack.
- Go back to the tabs at the top of the page, then select the "Deploy" tab.
- Select the Github deployment method.
- Search for your repository name, then click the "Connect" button to link your repository.
- At the bottom of that page, select deployment type: Automatic or Manual. By pressing "Enable Automatic Deploys," the project will redeploy to Heroku every time it is pushed to GitHub. If Manual deployments are preferred, then choose a branch to deploy ("main" by default) and press "Deploy Branch."  In either case, there will be a short wait while the project is deployed.

## Forking the Repository on GitHub

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/Estelindis/double-agent) that you want to fork.
2. In the upper right of the repository, click the "Fork" button.
3. A copy of the repository will now be available within your repositories.

Forking the GitHub repository makes a copy of the original repository on our GitHub account to view and/or make changes without affecting the original repository. This copy of the code can be edited without affecting the original code.

## Cloning the Repository on GitHub

1. In the upper section of the repository, click the dropdown named "Code."
2. In the "Clone with HTTPS" section, copy the URL.
3. Open Git Bash in your IDE of choice.
4. Change the current working directory to the location you want for the cloned directory.
5. Type "git clone" and paste the URL copied from GitHub.
6. After pressing Enter, the clone of your repository will be created.

# Used technologies and credits

## Languages
- Html.
- CSS.
- Python (Django).

## Python Libraries

- Text.
- Text.
- Text.

## Other Technologies
- [GitHub](https://github.com/)
- Text.
- Text.

## Credits
- Text.
- Text.
- [The Code Institute Slack](https://slack.com/) provided an invaluable database of information and community of support. I am particularly grateful to the msletb-nov-2021 cohort, our facilitator Kasia, and my mentor Darío. From my cohort, special mentions to Rhiannon McNulty and Rachel Rock, who are always ready and willing to provide feedback.
