# IS App
independent study tracking app

This web app is an independent study meeting tracking system. At the start of the 2021 school year California AB130 was passed changing the rules for independent study. The primary function of the app is to track weekly meetings with students to simplify complying with AB130. At the end of the week I have a summary of all meetings with each active student or students who missed meetings. Students with missing work or students who missed their meeting are highlighted in a different color on the week summary and the student detail view. 

Visit my <a href="https://autonomous-dev.herokuapp.com/project/2/">portfolio</a> to get a link to the live demo and guest sign on credentials.

I made and use this app with independent study classes I teach. As a real world problem I can see a lot of areas to grow the app.

For local hosting you can uncomment the sqlite db section in settings.py and comment out the production DB connection info. This project requires redis running for the auto complete student searches to work.

The root directory contains an untracked .env file with credentials. To make a new copy of this project work create a new file named .env in the root directory. The db credentials are formated for postgresql. Setting these values as heroku config vars works. The .env file must contain the following:

# .env

SECRET_KEY = 'your key goes here'

DB_name = 'your db name goes here'

DB_user = 'your db name goes here'

DB_password = 'your db password goes here'

DB_host = 'your db host goes here'

DB_port = 'your db port goes here'

REDIS_URL = 'redis://localhost'  # or address for production

DEBUG_MODE = 'Blank for false'
