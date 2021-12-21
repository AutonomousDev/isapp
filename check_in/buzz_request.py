import requests
import xmltodict
from django.db import models
from django.contrib.auth.models import User


def sanitize_key(my_dict):
    print("I was passed a: ", type(my_dict), "#############################################")
    my_dict = {key.strip(): item for key, item in my_dict.items()}
    return my_dict


class BuzzRequest:
    """This class makes API calls to the Buzz api and returns the requested data."""

    def __init__(self, app_user=None, token=""):
        self._user = app_user
        self._token = token

    def get_user(self):
        return self._user

    def get_token(self):
        return self._token

    def set_token(self, value):
        self._token = value

    def store_token_to_db(self):
        user = self.get_user()
        user.profile.ae_token = self.get_token()
        user.profile.save()

    def login(self, username, password, school):
        """Login to Accelerate Ed"""
        payload = {'cmd': 'login3', 'username': school + "/" + username, 'password': password, 'expireseconds': 10800}
        r = requests.post('https://accelerate-mccloud.api.agilixbuzz.com/cmd', data=payload)
        r_dict = xmltodict.parse(r.text, attr_prefix="")
        if r_dict['response']['code'] == 'InvalidCredentials':
            return r_dict['response']['code']
        self.set_token(r_dict['response']['user']['token'])
        self.store_token_to_db()

    def get_enrollments(self):
        payload = {"_token": self._token, 'cmd': 'listenrollmentsbyteacher', 'select': 'course,user'}
        r = requests.get('https://accelerate-mccloud.api.agilixbuzz.com/cmd', params=payload)
        r_dict = xmltodict.parse(r.text, attr_prefix='')

        # See the line below for an example of how to access the response data
        # print(r_dict['response']['enrollments']['enrollment'][0]['user']['firstname'])

        #print("**********************************************************")
        #print(r_dict['response']['enrollments']['enrollment'][0])
        return r_dict['response']['enrollments']['enrollment']

    def get_students(self):
        pass
