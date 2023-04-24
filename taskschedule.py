"""
Use this file to run automated import/export. Task scheduler will handle file activation.
"""

from edi.edi_api import EdiApi
import json
from datetime import date
import sys

client = EdiApi()

with open('./edi/today_invoices.json', 'r') as f:
    today_invoices = json.load(f)

date = date.today()
date = str(date).replace('-','')

unfiltered_data = client.search_onhold_today(date)

if not unfiltered_data["result"]:
    print("No data to report, pausing program.")
else:
    print("Data")

client.logout_of_api()

