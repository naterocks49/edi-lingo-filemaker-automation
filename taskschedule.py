"""
Use this file to run automated import/export. Task scheduler will handle file activation.
"""

from edi.edi_api import EdiApi
from filemaker.filemaker_api import FilemakerApi
import json
from datetime import date, datetime
import sys

with open('logs.txt', 'a') as f:
    f.write(f'Ran at {datetime.now()}\n')

client = EdiApi()
filemaker_client = FilemakerApi()

with open('./edi/today_invoices.json', 'r') as f:
    today_invoices = json.load(f)

date = '20230421'
'''date = date.today()
date = str(date).replace('-','')'''

if list(today_invoices.keys())[0] != date:
    today_invoices = {date:[]}
    with open('today_data.json', 'w') as f:
        json.dump([], f, indent=4)

print(today_invoices)

unfiltered_data = client.search_onhold_today(date)
filtered_data = []

if not unfiltered_data["result"]:
    print("No data to report, pausing program.")
else:
    for invoice in unfiltered_data['result']:
        if invoice['documentId'] not in today_invoices[date]:
            filtered_data.append(invoice)
            today_invoices[date].append(invoice['documentId'])
            print('ADD EXPORT HERE')

with open('today_data.json', 'r') as f:
    total_data = json.load(f)

total_data += filtered_data

filemaker_client.login()
for i in today_invoices:
    try:
        filemaker_client.post_new_entry("invoice_search", i)
    except ConnectionRefusedError:
        print('error')

for i in total_data:
    try:
        filemaker_client.post_new_entryo("invoice_get", i)
    except ConnectionRefusedError:
        print('error')

with open('today_data.json', 'w') as f:
    json.dump(total_data, f, indent=4)

with open('./edi/today_invoices.json', 'w') as f:
    json.dump(today_invoices, f, indent=4)

client.logout_of_api()