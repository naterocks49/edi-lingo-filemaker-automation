import unittest
import requests
from edi_api import EdiApi

class TestEdiApi(unittest.TestCase):

    i = EdiApi()

    def test_edi_api_login(self):
        self.i.logout_of_api()
        ses = self.i.login_to_api()
        self.assertIsNot(ses, '')

    def test_edi_logout(self):
        status = self.i.logout_of_api()
        self.assertEqual(status, 200)







