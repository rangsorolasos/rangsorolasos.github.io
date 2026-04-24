#!/usr/bin/env python3
import gspread
from google.oauth2.service_account import Credentials
import os
import json

# CONFIGURATION
SERVICE_ACCOUNT_FILE = os.path.expanduser('~/.serviceaccount.json')
SPREADSHEET_ID_ACTIVISTS = '1_UIuKEmZN5Nrc-wRzRf_cMEAeP8qRkcZjte_90f5zqU'
OUTPUT_FILE = os.path.expanduser('~/_data/activists.json')

# Scopes for read-only access
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

def table_to_json(data):
	headers = data[0]
	records = []
	
	for row in data[1:]:
	    record = {}
	    for i, value in enumerate(row):
	        record[headers[i]] = value
	    records.append(record)
	
	json_output = json.dumps(records, ensure_ascii=False, indent=2)
	return json_output

def get_client():
  creds = Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
  client = gspread.authorize(creds)
  return client
    
def get_table(client,tableId):
  sheet = client.open_by_key(tableId).sheet1
    
  all_values = sheet.get_all_values()
  non_empty_rows = [row for row in all_values if any(cell.strip() for cell in row)]
  return non_empty_rows

def main():
    client = get_client()
    non_empty_rows = get_table(client,SPREADSHEET_ID_ACTIVISTS)
    row_count = len(non_empty_rows)-1
    
    with open(OUTPUT_FILE, 'w') as f:
        f.write(f"""{{ "count": {row_count} }}""")
    
if __name__ == "__main__":
    main()
