import json
import pandas as pd

# Load JSON data
def JSON_to_CSV(data_path):

    with open(data_path, 'r') as f:
        data = json.load(f)

    data = json.dumps(data)
    # Open a CSV file in write mode
    df = pd.read_json(data)

    df.to_csv('output.csv', index=False)

    print("JSON data converted to CSV successfully!")

JSON_to_CSV('example_search_invoices.json')