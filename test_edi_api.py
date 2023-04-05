import unittest
import requests

LOGIN_URL = 'https://www.myweborders.com/rest/login'
BASE_API_URL = 'https://www.myweborders.com/rest/'

class TestEdiApi(unittest.TestCase):


    def test_edi_api_login(self):
        payload = {
            "userName": "molearygopal",
            "account": "BIE01",
            "userPass": "Bifido2021",
            "apiKey": "2N4IOZOAOSBEG43E6QAC",
        }
        res = requests.post(LOGIN_URL, payload)

        self.assertEqual(res.status_code, '200')






