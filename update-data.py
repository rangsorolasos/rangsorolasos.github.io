#!/usr/bin/env python3
import gspread
from google.oauth2.service_account import Credentials
import os
import json
from urllib.parse import urlparse

# CONFIGURATION
SERVICE_ACCOUNT_FILE = os.path.expanduser('~/.serviceaccount.json')
SPREADSHEET_ID_ACTIVISTS = '1_UIuKEmZN5Nrc-wRzRf_cMEAeP8qRkcZjte_90f5zqU'
SPREADSHEET_ID_SOCIAL = '13E2CEM18F0TXj8oXUQdHpciS52kiazxZaKwSSQyj-E0'
OUTPUT_ACTIVISTS = os.path.expanduser('~/_data/activists.json')
OUTPUT_ACTIVIST_LIST = os.path.expanduser('~/Private/.activists.json')
OUTPUT_SOCIAL = os.path.expanduser('~/_data/social.json')

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


def extract_domain(url: str) -> str:
    """
    Kinyeri a domain nevet az URL-ből (pl. 'https://www.example.com/path' -> 'example.com').
    www. előtag eltávolítva.
    Hibás URL esetén üres stringet ad vissza.
    """
    try:
        parsed = urlparse(url)
        hostname = parsed.hostname or ""
        # www. eltávolítása, ha jelen van
        if hostname.startswith("www."):
            hostname = hostname[4:]
        return hostname
    except Exception:
        return ""

def get_client():
  creds = Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
  client = gspread.authorize(creds)
  return client
    
def get_table(client,tableId):
  sheet = client.open_by_key(tableId).sheet1
    
  all_values = sheet.get_all_values()
  non_empty_rows = [row for row in all_values if any(cell.strip() for cell in row)]
  return non_empty_rows

def save_count(client,tableId,outputFile):
    non_empty_rows = get_table(client,tableId)
    row_count = len(non_empty_rows)-1
    
    with open(outputFile, 'w') as f:
        f.write(f"""{{ "count": {row_count} }}""")
    

def save_all(client,tableId,outputFile):
 data = get_table(client,tableId)
 row_count = len(data)-1
 headers = data[0]
 records = []
 for row in data[1:]:
   record = {}
   for i, value in enumerate(row):
    if headers[i] == "URL":
     record['domain'] = extract_domain(value)
    record[headers[i]] = value
   records.append(record)
  
 result = {'count': row_count, 'records': records}
 json_output = json.dumps(result, ensure_ascii=False, indent=2)

 with open(outputFile, 'w') as f:
    f.write(json_output)
    

def main():
    client = get_client()
    save_count(client,SPREADSHEET_ID_ACTIVISTS, OUTPUT_ACTIVISTS)
    save_all(client,SPREADSHEET_ID_ACTIVISTS, OUTPUT_ACTIVIST_LIST)
    save_all(client,SPREADSHEET_ID_SOCIAL, OUTPUT_SOCIAL)
if __name__ == "__main__":
    main()
