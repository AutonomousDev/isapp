import requests
import xmltodict

class Buzz_request():
    """TODO doc string"""

    def __init__(self):
        self._token = ""

    def get_token(self):
        return self._token

    def set_token(self, value):
        self._token = value

    def login(self, username, password):
        payload = {'cmd': 'login3', 'username': username, 'password': password}
        r = requests.post('https://accelerate-mccloud.api.agilixbuzz.com/cmd', data=payload)
        r_dict = xmltodict.parse(r.text)
        self.set_token(r_dict['response']['user']['@token'])


    def hello_requests(self):
        payload = {"_token": self._token, 'cmd': 'listenrollmentsbyteacher', 'select': 'course,user'}
        r = requests.get('https://accelerate-mccloud.api.agilixbuzz.com/cmd', params=payload)
        print(r.text)

        return r

buzz = Buzz_request()

print("calling login")
buzz.login('accelerate-mccloud/USERNAME', 'PASSWORD')
buzz.hello_requests()
