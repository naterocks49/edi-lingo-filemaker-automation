"""
Main Filemaker exporter.
"""
from .functions import encode_credentials
import requests

class FilemakerApi():
    
    def __init__(self):
        '''Initialize API variables'''
        self.BASE_URL = ""
        self.LOGIN_URL = self.BASE_URL + "/fmi/data/v2/databases/invoice-data/sessions"
        self.LOGOUT_URL = self.BASE_URL + "/fmi/data/v2/databases/invoice-data/sessions/"
        self.POST_DATA_URL = self.BASE_URL + '/fmi/data/v2/databases/invoice-data/layouts/'
        self.AUTH_TOKEN = None

    def login(self):
        '''Login to API - returns string with output message and sets auth token'''
        self.auth_header = {
            "Authorization": encode_credentials("Programmer", "12345"),
            "Content-Type": "application/json"
        }
        self.params = {}
        res = requests.post(self.LOGIN_URL, headers=self.auth_header, params=self.params)
        if res.status_code == '200':
            self.AUTH_TOKEN = res.json()['body']['response']['token']
            return "Login successful"
        else:
            self.AUTH_TOKEN = None
            return f"Login unsuccessful: {res.status_code}"
    
    def logout(self):
        '''Logout to API - returns string and sets AUTH token to None'''
        if not self.AUTH_TOKEN:
            return "NOT LOGGED IN"
        self.header = {
            "Content-Type": "application/json"
        }
        res = requests.delete(self.LOGOUT_URL + self.AUTH_TOKEN, headers=self.header)
        if res.json()['response'] == {}:
            self.AUTH_TOKEN = None
            return "SUCCESSFULLY LOGGED OUT"
    
    def post_new_entry(self, database, data):
        '''Posts single entry to database - equal mapping from lingo to filemaker'''
        if self.AUTH_TOKEN:
            self.auth_header = {
                "Authorization": encode_credentials("Programmer", "12345"),
                "Content-Type": "application/json"
            }
            self.params = data
            res = requests.post(self.POST_DATA_URL + f"{database}/records", headers=self.auth_header, params=self.params)
            if res.json['response']['recordId']:
                return "Success"
            else:
                return ConnectionRefusedError

