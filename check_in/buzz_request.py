import requests
import xmltodict
from users.models import Profile


class BuzzRequest:
    """This class makes API calls to the Buzz api and returns the requested data."""

    def __init__(self, _user, _token: str = ""):
        self._user = None
        self._token = ""

    def get_user(self):
        return self._user

    def get_token(self):
        return self._token

    def set_token(self, value):
        self._token = value

    def store_token_to_db(self):
        user = self.get_user()
        Profile.ae_token
        user.Profile.ae_token = self.get_token()


    def login(self, username, password, school):
        payload = {'cmd': 'login3', 'username': school+"/"+username, 'password': password, 'expireseconds': 10800}
        r = requests.post('https://accelerate-mccloud.api.agilixbuzz.com/cmd', data=payload)
        r_dict = xmltodict.parse(r.text)
        self.set_token(r_dict['response']['user']['@token'])


    def hello_requests(self):
        payload = {"_token": self._token, 'cmd': 'listenrollmentsbyteacher', 'select': 'course,user'}
        r = requests.get('https://accelerate-mccloud.api.agilixbuzz.com/cmd', params=payload)
        print(r.text)

        return r

