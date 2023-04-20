import json

with open('example_search_invoices.json', 'r') as f:
    data = json.load(f)

print(len(data))
