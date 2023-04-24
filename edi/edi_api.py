import requests
from datetime import time
import json
from .dateiterator import DateIterator


class EdiApi():

    LOGIN_URL = 'https://www.myweborders.com/rest/login'
    LOGOUT_URL = 'https://www.myweborders.com/rest/logout'

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
        return self.session_id

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

        return res.status_code

    def get_invoice_by_id(self, id):
        url = 'https://www.myweborders.com/rest/documents/invoice/'
        url += id
        header = {
            'sessionId': self.session_id,
            'Content-Type': 'application/json',
        }
        res = requests.get(url, headers=header)

        return res.json()['result']

    def search_invoice_filter_by_today(self):
        url = 'https://www.myweborders.com/rest/documents/invoice?'
        payload = {
            'statusList': 'OnHold',
            'documentDate': '20230420'
        }
        print(self.session_id)
        header = {
            'sessionId': self.session_id,
            'Content-Type': 'application/json',
        }
        res = requests.get(url, params=payload, headers=header)
        with open('example_search_invoices.json', 'w') as f:
            json.dump(res.json(), f, indent=4)
        return res.json()

    def grab_all_search_on_hold(self):
        start_date = '20230301'
        end_date = '20230420'
        date_iterator = DateIterator(start_date, end_date)
        final_dict = {}

        for date in date_iterator:
            url = 'https://www.myweborders.com/rest/documents/invoice?'
            payload = {
                'statusList': 'OnHold',
                'documentDate': date
            }
            print(self.session_id)
            header = {
                'sessionId': self.session_id,
                'Content-Type': 'application/json',
            }
            res = requests.get(url, params=payload, headers=header)
            for invoice in res.json()["result"]:
                final_dict[invoice["recordIdStr"]] = invoice

        with open('example_search_invoices.json', 'w') as f:
            json.dump(final_dict, f, indent=4)
        return res.json()

    def grab_all_get_on_hold(self):
        with open('example_search_invoices.json', 'r') as f:
            data = json.load(f)
        final_dict = {}

        for key in data.keys():
            url = 'https://www.myweborders.com/rest/documents/invoice/'
            url += key
            header = {
                'sessionId': self.session_id,
                'Content-Type': 'application/json',
            }
            res = requests.get(url, headers=header)

            final_dict[key] = res.json()['result']

        with open('example_get_invoice.json', 'w') as f:
            json.dump(final_dict, f, indent=4)
