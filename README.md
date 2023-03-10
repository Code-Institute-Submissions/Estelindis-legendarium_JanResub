# Legendarium - Project Portfolio 4 - Full Stack Toolkit
## by Siobhán Mooney

![Image of the site on various platforms.](/static/images/readme_responsive.jpg)

### [Click here to view the deployed app.](https://legendarium.herokuapp.com/)
### [Click here to view the repository.](https://github.com/Estelindis/legendarium)
### [Click here to view agile board.](https://github.com/Estelindis/legendarium/projects/1)

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
    4. [Manual Testing](#manual-testing)
5. [Future Features](#future-features)
6. [Deployment](#deployment)
    1. [Deploying to Heroku](#deploying-to-heroku)
    2. [Forking the Repository on GitHub](#forking-the-repository-on-github)
    3. [Cloning the Repository on GitHub](#cloning-the-repository-on-github)
7. [Used technologies and credits](#used-technologies-and-credits)
    1. [Technologies](#technologies)
    2. [Credits](#credits)


# About the project
Legendarium is an online story database for characters, places, objects, or anything else a writer can imagine.  

## User Goals
- Easily navigate a readable, accessible website from any platform.
- Read other users' stories without having to register or log in.
- Register to comment on stories and add them to one's library (this site's version of "likes").
- As a registered user, have the ability to create, read, update, and delete one's own stories.
- Have confidence that my content cannot be edited or deleted except by myself or an admin (in the latter case, only via admin panel).
- Save stories as drafts if they are not yet ready for publication.

## Owner Goals
- Present stories to users in a readable, accessible format.
- Include appealing features like images, notes, and categories in stories.
- CRUD (create, read, update, and delete) content via the admin panel, e.g. approve comments, delete stories with objectionable content.
- Have the ability to create, read, update, and delete categories via the front end.
- Prevent users from accessing unauthorised content via editing front end links.

# Design
In terms of visuals and data, Legendarium is inspired by the Code Institute "I Think Therefore I Blog" Codestar walkthrough project.  Following the lessons in that walkthrough to gain understanding of the underlying principles, I made informed choices about where to retain elements, where to make partial changes, and where to add new styling and models.

## Wireframes
Legendarium was originally imagined as a database for RPG character backstories.  Its initial wireframes reflect this vision, as does the name of its "chargen" app.  However, as development continued, it was reimagined as a database for stories of all kinds.   Further, the eventual site moved away from the initially planned large quantity of text on the index page, in favour of a more intuitive, image-centred approach.

![Mobile wireframe.](/static/images/mobile_wireframe.png)
![Desktop wireframe.](/static/images/desktop_wireframe.png)

## Data Models
The Comment model follows the Codestar walkthrough.  The Story model is adapted from the walkthrough's Post model, to include new elements such as an optional "notes" field and categories in which stories can be placed.  An original Category model is added to facilitate the categorization of stories.  While categories could have been added as a choice field in the Story model, a separate Category model allows admins to create, update, and delete categories without having to change any code.  

![Data model diagram.](/static/images/data_model_diagram.jpg)

# Agile Development
Legendarium was developed using agile methods, with the help of a [GitHub kanban board](https://github.com/Estelindis/legendarium/projects/1).

- Once tasks were identified, issues were added to the "to do" column.
- All tasks were labelled "must-have" or "could-have."  Must-have tasks were begun and completed preferentially.  As not every imagined feature can generally be completed with a project's timeframe, it is important to work on tasks in order of priority.
- When a task was being worked on, it was moved to the "in progress" column.
- Once sufficient content had been developed and tested to address the task, it was moved to the "done" column.
- At the end of the project work period, unfinished items were moved to a new category for future development.  This represents some of the possible future tasks that could be undertaken in a cloned version of the project.  
- All uncompleted tasks have the "could-have" label, while no "must-have" features remained unfinished.

![Index, URL.](/static/images/readme_kanban.jpg)

# Testing, Bugs, and Fixes

## HTML Validation
The html of the index (home page) and story_detail (individual story) pages were validated via [W3's Nu Html Checker](https://validator.w3.org/nu/).
Both deployed links and source html were tested. Additionally, the source code of various login-required pages was checked (including the admin-only categories listing and the pages for creating new stories and categories).

### Index, URL

![Index, URL.](/static/images/valid_html_url_index.jpg)

### Index, Source

![Index, source.](/static/images/valid_html_source_index.jpg)

### Story, URL

![Story, URL.](/static/images/valid_html_url_index.jpg)

### Story, Source

![Story, source.](/static/images/valid_html_source_index.jpg)

### Categories, Source

![Story, source.](/static/images/valid_html_source_categories.jpg)

### Add Category, Source

![Story, source.](/static/images/valid_html_source_category_add.jpg)

### Add Story, Source

![Story, source.](/static/images/valid_html_source_story_add.jpg)

## CSS Validation
The CSS of the index (home page) and story_detail (individual story) pages were validated via [W3's Jigsaw Validator](https://jigsaw.w3.org/css-validator/).
Both deployed links and the source style.css were tested.

### Style.css, Source

![Index, source.](/static/images/valid_css_source.jpg)

### Index, URL

![Index, URL.](/static/images/valid_css_url_index.jpg)

### Story, URL

![Story, URL.](/static/images/valid_css_url_index.jpg)

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

## Manual Testing
User and owner goals were tested to ensure that the aims of the project were achieved.

### Goal: Accessible Content
This condenses the following goals:
- (User) Easily navigate a readable, accessible website from any platform.
- (User) Read other users' stories without having to register or log in.
- (Owner) Present stories to users in a readable, accessible format.

To test this functionality, an unregistered user follows these steps:
- Navigate to Legendarium.
- Broswe stories by scrolling down (and, if desired, navigating to the next pages of stories).
- Click or press on the name of a story to read the individual story.  This provides the user reading functionality.
- Return to browsing via the navbar, which is always accessible via its fixed position.

On following these steps, did the expected results occur?
- Yes, tests passed, as the following images show.  The index is shown in desktop view, which clearly demonstrates that the user is not logged in.  A further screenshot of a story detail page is also provided, this time in tablet view.  Text is legible.  Colours provide sufficient contrast for accessibility, yet fade from view to allow content to take the foreground.

![Index, desktop view](/static/images/screenshot_index.jpg)

![Story detail, tablet view](/static/images/screenshot_story_detail.jpg)

### Goal: User Registration
- (User) Register to comment on stories and add them to one's library (this site's version of "likes").

To test this functionality, a user follows these steps:
- Navigate to Legendarium.
- Click or press Register in the navbar.
- Input a username and password (email is optional).
- On successful registration, the user is now logged in.
- The logged in user can freely add and remove stories from their library (a "like" system).  This provides updating/deleting functionality.
- The logged in user can also create comments on posts, after which a message states the comment is awaiting approval.  This provides the user with creating functionality.
- The logged in user can sign out by clicking/pressing Logout in the navbar. After confirming, the user is successfully logged out.

On following these steps, did the expected results occur?
- Yes, tests passed, as the following images show.

![Manual testing screenshot 01_01](/static/images/test01_01.jpg)

![Manual testing screenshot 01_02](/static/images/test01_02.jpg)

![Manual testing screenshot 01_03](/static/images/test01_03.jpg)

![Manual testing screenshot 01_03a](/static/images/test01_03a.jpg)

![Manual testing screenshot 01_03b](/static/images/test01_03b.jpg)

![Manual testing screenshot 01_04](/static/images/test01_04.jpg)

### Goal: Manage Stories
This condenses the following goals:
- (User) Save stories as drafts if they are not yet ready for publication.
- (Owner) CRUD (create, read, update, and delete) content via the admin panel, e.g. approve comments, delete stories with objectionable content.
- (Owner) Include appealing features like images, notes, and categories in stories.


To test Create functionality via the admin panel, an admin follows these steps:
- Navigate to the Legendarium Admin area and log in as an Admin.
- Under the "chargen" heading, in the Stories row, click or press Add.
- Fill in the required fields of the story form, including name. The form shows that notes and an image can be added, but are not required.
- A story's default status is Draft.  The story can be saved as a Draft, to be edited at leisure, or can be set to Published immediately.
- Click/press Save in the bottom right corner.  The story has now been created.
- Return to the non-admin site by pressing/clicking View Site in the top right. If the story was saved as Draft, it will not be seen in the index. If it was saved as Published, it will appear immediately among the other stories.

On following these steps, did the expected results occur?
- Yes, tests passed, as the following images show.

![Manual testing screenshot 01_01](/static/images/test03_01.jpg)

![Manual testing screenshot 01_02](/static/images/test03_02.jpg)

![Manual testing screenshot 01_03](/static/images/test03_03.jpg)

To test Update functionality, an admin follows these steps:
- Navigate to the Legendarium Admin area and log in as an Admin.
- Under the "chargen" heading, in the Stories row, click or press Change.
- Click or press the name of the story to change.  Previously created content for that story can now be edited.
- Once saved, changes to the story will be visible on the live site if that story is Published.

On following these steps, did the expected results occur?
- Yes, tests passed, as the following image shows. Most images of story editing are not notably distinct from new story creation, but this image shows a record of changes to stories.

![Manual testing screenshot 01_01](/static/images/test03_07.jpg)

To test Delete functionality, an admin follows these steps:
- Navigate to the Legendarium Admin area and log in as an Admin.
- Under the "chargen" heading, in the Stories row, click or press Change.
- Select stories via the checkbox beside each name in the list. If many stories are present, the list can be filtered via the search bar.
- Once one or more stories are selected, choose "delete selected stories" from the Action dropdown menu. The deletion can then be confirmed or cancelled.
- Once deleted, a Published story that was previously visible on the live site can no longer be viewed.

On following these steps, did the expected results occur?
- Yes, tests passed, as the following images show.

![Manual testing screenshot 01_01](/static/images/test03_04.jpg)

![Manual testing screenshot 01_02](/static/images/test03_05.jpg)

![Manual testing screenshot 01_03](/static/images/test03_06.jpg)

### Goal: Front end CRUD functionality
This condenses the following goals:
- (User) As a registered user, have the ability to create, read, update, and delete one's own stories. 
- (Owner) Have the ability to create, read, update, and delete categories via the front end.

To test front-end Create and Read functionality for stories, both a regular user and an admin can follow these steps:
- If not already logged in, log in via the navbar.
- Navigate to "Create a Story" in the navbar.
- Add required content to the story form, plus any additional optional content according to one's preference.
- Click "save" at the bottom of the form.
- If "published" status was chosen during creation, the newly created story can now be viewed in the story index / home page.

![Manual testing: front-end create story screenshot](/static/images/test_create_story.jpg)

To test front-end Update functionality for stories, both a regular user and an admin can follow these steps:
- If not already logged in, log in via the navbar. On successful login, the user will be redirected to the story index / home page.
- While logged in, any story of whom the current user is the author will now display an "edit" link.
- Choose a self-authored story to edit, then click its associated "edit" link.
- A form will appear allowing the user to edit that story. The edit can be cancelled or saved at the bottom of the form.
- Returning to the story index / home page and clicking on the same story, any updates made can now be viewed.

To test front-end Delete functionality for stories, both a regular user and an admin can follow these steps:
- If not already logged in, log in via the navbar. On successful login, the user will be redirected to the story index / home page.
- While logged in, any story of whom the current user is the author will now display a "delete" link.
- Choose a self-authored story to delete, then click its associated "delete" link.
- The user will be asked if they really wish to delete the story or cancel the deletion. If "delete" is chosen, the story is deleted.  
- Returning to the story index / home page, any deleted story will no longer be seen.

![Manual testing: front-end edit/delete story screenshot](/static/images/test_edit_delete_story.jpg)
![Manual testing: delete confirmation screenshot](/static/images/test_delete_confirm.jpg)

To test front-end Create and Read functionality for categories, an admin follows these steps:
- If not already logged in, log in as an admin via the navbar.
- Navigate to "Create a Category" in the navbar.
- Add required content to the category form, plus any additional optional content according to one's preference.
- Click "save" at the bottom of the form.
- The newly created category can now be viewed by an admin by navigating to "Categories" via the navbar.

![Manual testing: front-end create category screenshot](/static/images/test_create_category.jpg)

To test front-end Update functionality for categories, an admin follows these steps:
- If not already logged in, log in as an admin via the navbar.
- Navigate to "Categories" in the navbar.
- Choose a category to edit, then click its associated "edit" link.
- A form will appear allowing the admin to edit that category. The edit can be cancelled or saved at the bottom of the form.
- Returning to the categories page, any updates made can now be viewed.

To test front-end Delete functionality for categories, an admin follows these steps:
- If not already logged in, log in as an admin via the navbar.
- Navigate to "Categories" in the navbar.
- Choose a category to delete, then click its associated "delete" link.
- The admin will be asked if they really wish to delete the category or cancel the deletion. If "delete" is chosen, the category is deleted.  
- Returning to the categories page, any deleted category will no longer be seen.

### Goal: Front end content security
This condenses the following goals:
- (User) Have confidence that my content cannot be edited or deleted except by myself or an admin (in the latter case, only via admin panel).
- (Owner) Prevent users from accessing unauthorised content via editing front end links.

To test that (from the front end) users cannot edit or delete stories they have not authored, follow these steps:
- If not already logged in, log in via the navbar.
- Choose a self-authored story to edit or delete, then click its associated "edit" or "delete" link.
- In the browser's URL bar, edit the URL to change the ID of the story being edited/deleted to a different ID, one associated with an existent story not authored by the current user.
- On pressing enter in the URL bar to attempt to load the edit/delete page of another user's story, a 403 page will display instead, informing the user that this action is forbidden.
- The user can then return to the story index / home page.
- To test that another user's stories cannot be edited or deleted from the front end even by an admin, repeat these steps while logged in as an admin.

![Manual testing: custom 403 screenshot](/static/images/test_403.jpg)

To test that (from the front end) non-admin users cannot access category CRUD functionality (apart from reading categories as part of stories, or applying an existing category to a story they create), follow these steps:
- If already logged in as an admin, log out, then log back in as a non-admin user.
- In the browser's URL bar, edit the URL to the following: https://legendarium.herokuapp.com/categories/
- On pressing enter in the URL bar to attempt to load the categories page, a 403 page will display instead, informing the user that this action is forbidden.
- The user can then return to the story index / home page.
- To test that categories also cannot be edited or deleted by non-admin users, repeat these steps, instead pasting category edit or delete links into the browser's URL bar.
- Category edit links have the following format: https://legendarium.herokuapp.com/categories/edit/[integer representing an existent category id]
- Category delete links have the following format: https://legendarium.herokuapp.com/categories/delete/[integer representing an existent category id]

![Manual testing: screenshot of editing a forbidden url into the browser url bar](/static/images/test_forbidden_url.jpg)

# Future Features
- Users should be able to view a list of stories added to their libraries.
- Users should be able to view stories filtered by category.
- Users should be able to add (and remove) tags for their own stories, so they can categorize their content beyond the limits of the standard admin-controlled categories.
- Admins could potentially be made able to carry out all admin activities without having to access the built-in Django admin panel.  In this scenario, admin functions would appear on the front-end when admins are logged in (e.g. an admin viewing a page with comments would have the option to approve comments directly, from that page).  This may however have the disadvantage of removing the particular "paper trail" that is built into the admin view, if (for instance) admins are allowed to edit or delete any user-created content from the front end.

## Progress Towards Future Features

- Some preliminary attempts were made to display a list of stories a user has added to their library.  While some success was achieved at returning a list, it did not attain a user-friendly form within the time period for the project.

![Future feature library display](/static/images/future_feature01.jpg)

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
- Broadly speaking, manual deployment is preferred for this kind of project, so that DEBUG in settings.py can be set to True during development but False during deployment.

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

## Technologies
- [HTML5](https://en.wikipedia.org/wiki/HTML)
- [CSS3](https://en.wikipedia.org/wiki/CSS)
- [Python](https://en.wikipedia.org/wiki/Python_(programming_language))
- [Django](https://www.djangoproject.com/)
- [Heroku](https://www.heroku.com)
- [Heroku PostgreSQL](https://www.heroku.com/postgres)
- [Cloudinary](https://cloudinary.com/)
- [Bootstrap 5.0.1](https://getbootstrap.com/)
- [Bootstrap Icons 1.9.1](https://icons.getbootstrap.com/)
- [Google Fonts](https://fonts.google.com)
- [GitHub](https://github.com/)

## Credits
- The Code Institute's Codestar blog walkthrough provided development guidance and instruction, demonstrating how to create a site in Django and providing a starting point from which to add and elaborate further content.
- [The Code Institute Slack](https://slack.com/) provided an invaluable database of information and community of support. I am particularly grateful to the msletb-nov-2021 cohort, our facilitator Kasia, and my mentor Darío.
