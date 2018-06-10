import gspread
from oauth2client.service_account import ServiceAccountCredentials
import json
import pprint

pp = pprint.PrettyPrinter()

# connect to google api and open NZ fees spreadsheet
scope = ['https://www.googleapis.com/auth/drive.readonly']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(creds)

nzfees_worksheet = client.open('NZ fees')
nzfees_worksheet_list = nzfees_worksheet.worksheets()

# list worksheets only with annual expenses
def has_year_in_title(sheet):
    return sheet.title.find('201') == 0

def find_fees_worksheets():
    return filter(has_year_in_title, nzfees_worksheet_list)

filtered_nzfees_worksheet_list = list(find_fees_worksheets())

all_years_list = []
i = 0
while (i < len(filtered_nzfees_worksheet_list)):
    all_years_list.append(filtered_nzfees_worksheet_list[i].title)
    i += 1

# list monthly expenses in 2013
year_2013_worksheet = nzfees_worksheet.worksheet("2013")
year_2013_cells = []

def is_expense(cell):
    return cell.find('$') == 0

for month_expense_cell in range(2, 36):
    year_2013_cells.append(year_2013_worksheet.cell(16, month_expense_cell).value)

def find_year_2013_monthly_expenses():
    return filter(is_expense, year_2013_cells)
year_2013_monthly_expenses = list(find_year_2013_monthly_expenses())
pp.pprint('year 2013: ' + str(year_2013_monthly_expenses))

# put 2013 monthly expenses into json file
year2013_monthly_data = {}
year2013_month = {}
year2013_mothly_list = []
months_list = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

m = 0
for m in range (0, 12):
    year2013_month[months_list[m]] = year_2013_monthly_expenses[m]

year2013_mothly_list.append(year2013_month)
pp.pprint('year2013_mothly_list' + str(year2013_mothly_list))
year2013_monthly_data['year 2013'] = year2013_mothly_list
year2013_monthly_json = json.dumps(year2013_monthly_data)

with open('year2013_monthly.json', 'w') as year2013_monthly:
    json.dump(year2013_monthly_json, year2013_monthly)
