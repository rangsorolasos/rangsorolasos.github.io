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
    # Authenticate with the service account
    creds = Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
    client = gspread.authorize(creds)

    # Open the sheet (by name or ID)
    sheet = client.open(SPREADSHEET_NAME_OR_ID).sheet1

    # Get all values and count rows (excluding empty rows at bottom)
    all_values = sheet.get_all_values()
    # Remove trailing empty rows if you want only rows with data
    non_empty_rows = [row for row in all_values if any(cell.strip() for cell in row)]
    row_count = len(non_empty_rows)

    # Write the count to the output file
    with open(OUTPUT_FILE, 'w') as f:
        f.write(str(row_count))

    # Optional: also print to console for debugging
    print(f"Row count: {row_count}")

if __name__ == "__main__":
    main()
