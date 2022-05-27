# Deployment

## Initial Deployment
Below are the steps I took to deploy the site to Heroku and any console commands required to initiate it.
### Create repository:
1. Create a new repository in GitHub and clone it locally following [these instructions](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository)
    * ***Note*** - If you are cloning my project, then you can skip all pip installs below and just run the following command in the terminal to install all the required libraries/packages at once:
       * ```pip3 install -r requirements.txt```
    * ***IMPORTANT*** -  If developing locally on your device, ensure you set up/activate the virtual environment ([see below](#setting-up-the-workspace-to-be-done-locally-via-the-console-of-your-chosen-editor)) before installing/generating the requirements.txt file; failure to do this will pollute your machine and put other projects at risk
   
### Setting up the Workspace on Gitpod:

1. Install Django version 3.2 and gunicorn:
    * ```pip3 install 'django<4' gunicorn ```

1. Install supporting libraries:
    * ```pip3 install dj_database_url psycopg2```
    * ```pip3 install dj3-cloudinary-storage```
1. Create requirements.txt:
    * ```pip3 freeze --local > requirements.txt```
1. Create an empty folder for your project in your chosen location.
1. Create a project in the above folder:
    * django-admin startproject <PROJECT_NAME> (in the case of this project, the project name was "linktree")
1. Create an app within the project:
    * ```python manage.py startapp APP_NAME``` (in the case of this project, the app name was "links, accounts")
1. Add a new app to the list of installed apps in setting.py
1. Migrate changes: 
    * ```python manage.py migrate```
1. Test server works locally: 
    * ```python manage.py runserver```  (You should see the default Django success page)

### Create Heroku App:
The below works on the assumption that you already have an account with [Heroku](https://id.heroku.com/login) and are already signed in.
1. Create a new Heroku app:
    * Click "New" in the top right-hand corner of the landing page, then click "Create new app."
1. Give the app a unique name:
    * Will form part of the URL (in the case of this project, I called the Heroku app linktree)
1. Select the nearest location:
    * For me, this was Europe.
1. Add Database to the Heroku app:
    * Navigate to the Resources tab of the app dashboard. Under the heading "Add ons," search for "Heroku Postgres" and click on it when it appears. 
    * Select "Hobby Dev - Free" from the "plan name" drop-down menu and click "Submit Order Form."
1. From your editor, go to your projects settings.py file and copy the SECRET_KEY variable. Add this to the same name variable under the Heroku App's config vars.
    * left box under config vars (variable KEY) = SECRET_KEY
    * right box under config vars (variable VALUE) = Value copied from settings.py in project.

### Creating Environmental Variables Locally:
1. Install dotenv package:
    * pip install python-dotenv (not required for Gitpod)
1. On your local machine/workspace, create a file called "env.py" at the same level as settings.py and add this to the .gitignore file.
1. From the Heroku app settings tab, click "reveal config vars" and copy the value of the variable DATABASE_URL. Add this value to a variable called DATABASE_URL in your create env.py file:
    * ``` DATABASE_URL=PastedValueFromHerokuHere ``` - ***(note that with the dotenv package no quotation marks are required)***
1. From your projects settings.py file, copy the SECRET_KEY value and assign it to a variable called SECRET_KEY in your .env file
    * ``` SECRET_KEY=PastedValueFromYourProjectsSettings.pyFile ```
1. Add DEVELOPMENT variable to env.py file:
    * ``` DEVELOPMENT=development ```
1. Add CLOUDINARY_URL variable to env.py file:
    * Log into cloudinary and from the dashboard copy the API Environmental Variable.
    * Add to env.py file like below
        * ``` CLOUDINARY_URL=PastedApiEnvironmentalVariable ```


### Setting up setting.py File:
1. At the top of your settings.py file, add the following snippet immediately after the other imports:
    ``` 
        import os
        import dj_database_url
        if os.path.isfile("env.py"):
            import env
        SECRET_KEY = os.environ.get("SECRET_KEY")
        DEBUG = (os.environ.get('DEBUG_VALUE') == 'True')
    ``` 
1. Delete the value from the setting.py DATABASES section and replace it with the following snippet to link up the Heroku Postgres server:  
   
    ```
    DATABASES = {
    'default': dj_database_url.parse(os.environ.get("DATABASE_URL"))
    }
    ```

1. Add Cloudinary libraries to the installed apps section of settings.py file:
   
   ```
    INSTALLED_APPS = [
   …,
   'cloudinary_storage',
   'django.contrib.staticfiles',
   'cloudinary',
   …,
   ]
   (note: order is important)
   ```

1. Tell Django to use Cloudinary to store media and static files by placing this snippet under the comments indicated below:
```
    # Static files (CSS, JavaScript, Images)
    # https://docs.djangoproject.com/en/3.2/howto/static-files/
    STATIC_URL = '/static/'
    STATICFILES_STORAGE = 'cloudinary_storage.storage.StaticHashedCloudinaryStorage'
    STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static/')]
    STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
    MEDIA_URL = '/media/'
    DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'
```

1. Under the line with BASE_DIR, link templates directly in Heroku via settings.py:
   * ``` TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates') ```

1. Within TEMPLATES array, add ``` 'DIRS':[TEMPLATES_DIR] ``` like the below example:
```
   TEMPLATES = [
       {
           …,
           'DIRS': [TEMPLATES_DIR],
           …,
          
        },
       },
   ]
```
1. Add allowed hosts to settings.py:
    * ``` ALLOWED_HOSTS = ["PROJECT_NAME.herokuapp.com", "localhost"] ``` 

1. Create Procfile at the top level of the file structure and insert the following:
    * ``` web: gunicorn PROJECT_NAME.wsgi ```

1. Make an initial commit and push the code to the GitHub Repository.
    * ```git add .```
    * ```git commit -m "Initial deployment"```
    * ```git push```

### Set up Heroku for use via the console.
1. Click on Account Settings (under the avatar menu)
1. Scroll down to the API Key section and click Reveal. Copy the API key.
1. Log in to Heroku via the console and enter your details.
    * heroku login-i
    * When prompted, enter your Heroku username
    * Enter copied API key as the password

1. Get your app name from Heroku
    * ```heroku apps```
1. Set Heroku remote
    * ```heroku git:remote -a <app_name>```
1. Add, Commit, Pust to GitHub:
    * ```git add . && git commit -m "Deploy to Heroku via CLI"```
1. Push to GitHub and Heroku
    * ```git push origin main```
    * ```git push heroku main ``` 

## Cloning on a Local machine or Via Gitpod Terminal
1. Navigate to the [GitHub repository](https://github.com/fergalquinn77/ci-project4-fq-linkbuilder.git), and follow [these steps to clone the project](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository) into your IDE of choice.   
   
   * **Gitpod** only **requires** you to have the **web extension** installed and **click** the **green Gitpod button** from the repositories main page. If you are **using Gitpod**, please **skip step 2** below as you do not require a virtual environment to protect your machine.  
  
1. **Create** the **virtual environment** with the terminal command **```python3 -m venv venv```.** Once complete add the "venv" file to you're ".gitignore" file and use the terminal command **```venv\Scripts\activate.bat``` to activate it.**
   
   * ***IMPORTANT*** If developing locally on your device, ensure you **set up/activate the virtual environment before installing/generating the requirements.txt file**; failure to do this will pollute your machine and put other projects at risk.
 
1. **Install the requirements** listed in requirements.txt using the terminal command  **```pip3 install -r requirements.txt```**
   * Kindly note that since I developed the project from scratch and installed the required libraries as I progressed **I have already included a requirements.txt for this app** by using the terminal command **```pip3 freeze > requirements.txt```** to generate it.

1. **[Create your own Heroku app](#create-heroku-app)**, and update allowed hosts in settings.py.
   
1. **[Create your .env file](#creating-environmental-variables-locally).

1. **Run server locally** with ``` python mange.py runserver ```

[Back to Readme](README.md)