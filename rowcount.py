#!/usr/bin/env python3
import gspread
from google.oauth2.service_account import Credentials
import os

# CONFIGURATION
SERVICE_ACCOUNT_FILE = os.path.expanduser('~/.serviceaccount.json')
SPREADSHEET_NAME_OR_ID = '1_UIuKEmZN5Nrc-wRzRf_cMEAeP8qRkcZjte_90f5zqU'
OUTPUT_FILE = 'sheet_row_count.txt'

# Scopes for read-only access
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

def main():
    creds = Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
    client = gspread.authorize(creds)
    
    # Open directly by ID – no name lookup, no extra permissions needed
    sheet = client.open_by_key(SPREADSHEET_NAME_OR_ID).sheet1
    
    all_values = sheet.get_all_values()
    non_empty_rows = [row for row in all_values if any(cell.strip() for cell in row)]
    row_count = len(non_empty_rows)
    
    with open(OUTPUT_FILE, 'w') as f:
        f.write(str(row_count))
    
    print(non_empty_rows)

    print(f"Row count: {row_count}")

if __name__ == "__main__":
    main()
