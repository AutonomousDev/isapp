# isapp
Independant study tracking app


This project is a Django app designed to track independant study student meetings. 

For local hosting you can uncomment the sqlite db section in settings.py and comment out the production DB connection info. This project requires redis running for the auto complete student searches to work.

The root directory contains an untracked .env file with credentials. To make a new copy of this project work create a new file named .env in the root directory. The db credentials are formated for postgresql. Setting these values as heroku config vars works. The .env file must contain the following:


SECRET_KEY = 'your key goes here'

DB_name = 'your db name goes here'

DB_user = 'your db name goes here'

DB_password = 'your db password goes here'

DB_host = 'your db host goes here'

DB_port = 'your db port goes here'

REDIS_URL = 'redis://localhost'  # or address for production
