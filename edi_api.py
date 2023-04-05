import requests
from datetime import time


class EdiApi():

    LOGIN_URL = 'https://www.myweborders.com/rest/login'
    LOGOUT_URL  = 'https://www.myweborders.com/rest/logout'

    def __init__(self):
        self.user_payload = {
            "userName": "molearygopal",
            "account": "BIE01",
            "userPass": "Bifido2021",
            "apiKey": "2N4IOZOAOSBEG43E6QAC",
        }
        res = requests.post(self.LOGIN_URL, json=self.user_payload)
        self.session_id = res.json()['sessionId']
        print("Logged into EDI API")

    def login_to_api(self):
        if self.session_id != '':
            print('Already logged in!')
        else:
            res = requests.post(self.LOGIN_URL, json=self.user_payload)
            self.session_id = res.json()['sessionId']
            print("Logged into EDI API")

    def logout_of_api(self):

        if not self.session_id:
            return "Not logged in."

        headers = {
        'Content-Type': 'application/json',
        'sessionId': self.session_id
        }

        res = requests.post(self.LOGOUT_URL, headers=headers)
        self.session_id = ''
        print('Logging out')

        return res.json()

    def search_order_filter_by_today(self):
        url = 'https://www.myweborders.com/rest/documents/order?'
        payload = {
            'statusList':'OpenAll',
            'fulfillAuthStatus': 'Approved',
            'documentDate': '20240404',
        }
        print(self.session_id)
        header = {
            'sessionId': self.session_id,
            'Content-Type': 'application/json',
        }
        res = requests.post(url, params=payload, headers=header)

        print(res.url)
        return res.content
