# Test File to rough test python <-> Google Sheets Connection

import gspread

# Connect to Google Sheets
ServiceAcc = gspread.service_account(filename='EquiptmentTracker.json')
sheet = ServiceAcc.open("Equiptment Tracker")

worksheet = sheet.worksheet("Monitoring") 

print("Rows: ", worksheet.row_count)
print("Cols: ", worksheet.col_count)
