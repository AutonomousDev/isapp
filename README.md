# isapp
Independant study tracking app


This project is a Django app designed to track independant study student meetings. 

The root directory contains an untracked .env file with credentials. To make a new copy of this project work create a new file named .env in the root directory. The db credentials are formated for postgresql. The .env file must contain the following:

# .env
# Django SECRET_KEY
SECRET_KEY = 'your key goes here'

# DB Login info
DB_name = 'your db name goes here'
DB_user = 'your db name goes here'
DB_password = 'your db password goes here'
DB_host = 'your db host goes here'
DB_port = 'your db port goes here'
