import requests
import json

body = {
    'applicationId': '',
    'username': '',
    'password': '',
    'grant_type': '',
    'client_id': ''
}
headers = {u'content-type': u'application/x-www-form-urlencoded'}
url = 'https://site/authentication/account/signin'

data = requests.post(url, data=body, headers=headers).text

class Access(object):
 def __init__(self, json_content):
        data = json.loads(json_content)
        for key, value in data.items():
            self.__dict__[key] = value   

access = Access(data)

print(access.access_token)