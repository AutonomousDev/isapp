release: python manage.py makemigrations
release: python manage.py migrate
web: gunicorn isapp.wsgi --log-file -
heroku ps:scale web=1