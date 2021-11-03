import requests
import xmltodict


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
        payload = {'cmd': 'login3', 'username': school + "/" + username, 'password': password, 'expireseconds': 10800}
        r = requests.post('https://accelerate-mccloud.api.agilixbuzz.com/cmd', data=payload)
        r_dict = xmltodict.parse(r.text)
        if r_dict['response']['@code'] == 'InvalidCredentials':
            return r_dict['response']['@code']
        self.set_token(r_dict['response']['user']['@token'])
        self.store_token_to_db()

    def hello_requests(self):
        payload = {"_token": self._token, 'cmd': 'listenrollmentsbyteacher', 'select': 'course,user'}
        r = requests.get('https://accelerate-mccloud.api.agilixbuzz.com/cmd', params=payload)
        print(r.text)
        return r
