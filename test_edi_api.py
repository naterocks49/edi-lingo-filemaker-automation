import unittest
import requests

LOGIN_URL = 'https://www.myweborders.com/rest/login'
BASE_API_URL = 'https://www.myweborders.com/rest/'

class TestEdiApi(unittest.TestCase):


    def test_edi_api_login(self):
        payload = {
            "userName": "",
            "account": "",
            "userPass": "",
            "apiKey": "",
        }
        res = requests.post(LOGIN_URL, payload)

        print(res.status_code)






