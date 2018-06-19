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

months_list = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
all_years_list = []
i = 0
while (i < len(filtered_nzfees_worksheet_list)):
    all_years_list.append(filtered_nzfees_worksheet_list[i].title)
    i += 1

def is_expense(cell):
    return cell.find('$') == 0

def create_expenses_array(expense_cell, year_cells, year_worksheet):
    for month_expense_cell in range(2, 36):
        year_cells.append(year_worksheet.cell(expense_cell, month_expense_cell).value)

def find_monthly_expenses_for_year(year_cells):
    return filter(is_expense, year_cells)

def create_expense_list_with_month_name(year_month, year_monthly_expenses):
    m = 0
    for m in range (0, 12):
        year_month[months_list[m]] = year_monthly_expenses[m]

# list monthly expenses in 2013
year_2013_worksheet = nzfees_worksheet.worksheet("2013")
year_2013_cells = []

create_expenses_array(16, year_2013_cells, year_2013_worksheet)

year_2013_monthly_expenses = list(find_monthly_expenses_for_year(year_2013_cells))

# put 2013 monthly expenses into json file
year2013_monthly_data = {}
year2013_month = {}
year2013_mothly_list = []

create_expense_list_with_month_name(year2013_month, year_2013_monthly_expenses)

year2013_mothly_list.append(year2013_month)
pp.pprint('year2013_mothly_list' + str(year2013_mothly_list))
year2013_monthly_data['year 2013'] = year2013_mothly_list

######
# list monthly expenses in 2014
year_2014_worksheet = nzfees_worksheet.worksheet("2014")
year_2014_cells = []

create_expenses_array(18, year_2014_cells, year_2014_worksheet)

year_2014_monthly_expenses = list(find_monthly_expenses_for_year(year_2014_cells))

# put 2014 monthly expenses into json file
year2014_monthly_data = {}
year2014_month = {}
year2014_mothly_list = []

create_expense_list_with_month_name(year2014_month, year_2014_monthly_expenses)

year2014_mothly_list.append(year2014_month)
pp.pprint('year2014_mothly_list' + str(year2014_mothly_list))
year2014_monthly_data['year 2014'] = year2014_mothly_list

######
# list monthly expenses in 2015
year_2015_worksheet = nzfees_worksheet.worksheet("2015")
year_2015_cells = []

create_expenses_array(20, year_2015_cells, year_2015_worksheet)

year_2015_monthly_expenses = list(find_monthly_expenses_for_year(year_2015_cells))

# put 2015 monthly expenses into json file
year2015_monthly_data = {}
year2015_month = {}
year2015_mothly_list = []

create_expense_list_with_month_name(year2015_month, year_2015_monthly_expenses)

year2015_mothly_list.append(year2015_month)
pp.pprint('year2015_mothly_list' + str(year2015_mothly_list))
year2015_monthly_data['year 2015'] = year2015_mothly_list

######
# list monthly expenses in 2016
year_2016_worksheet = nzfees_worksheet.worksheet("2016")
year_2016_cells = []

create_expenses_array(20, year_2016_cells, year_2016_worksheet)

year_2016_monthly_expenses = list(find_monthly_expenses_for_year(year_2016_cells))

# put 2016 monthly expenses into json file
year2016_monthly_data = {}
year2016_month = {}
year2016_mothly_list = []

create_expense_list_with_month_name(year2016_month, year_2016_monthly_expenses)

year2016_mothly_list.append(year2016_month)
pp.pprint('year2016_mothly_list' + str(year2016_mothly_list))
year2016_monthly_data['year 2016'] = year2016_mothly_list

######
# list monthly expenses in 2017
year_2017_worksheet = nzfees_worksheet.worksheet("2017")
year_2017_cells = []

create_expenses_array(20, year_2017_cells, year_2017_worksheet)

year_2017_monthly_expenses = list(find_monthly_expenses_for_year(year_2017_cells))

# put 2017 monthly expenses into json file
year2017_monthly_data = {}
year2017_month = {}
year2017_mothly_list = []

create_expense_list_with_month_name(year2017_month, year_2017_monthly_expenses)

year2017_mothly_list.append(year2017_month)
pp.pprint('year2017_mothly_list' + str(year2017_mothly_list))
year2017_monthly_data['year 2017'] = year2017_mothly_list

######
# list monthly expenses in 2018
year_2018_worksheet = nzfees_worksheet.worksheet("2018")
year_2018_cells = []

create_expenses_array(20, year_2018_cells, year_2018_worksheet)

year_2018_monthly_expenses = list(find_monthly_expenses_for_year(year_2018_cells))

# put 2018 monthly expenses into json file
year2018_monthly_data = {}
year2018_month = {}
year2018_mothly_list = []

create_expense_list_with_month_name(year2018_month, year_2018_monthly_expenses)

year2018_mothly_list.append(year2018_month)
pp.pprint('year2018_mothly_list' + str(year2018_mothly_list))
year2018_monthly_data['year 2018'] = year2018_mothly_list

all_years_monthly_expenses = {**year2013_monthly_data, **year2014_monthly_data, **year2015_monthly_data, **year2016_monthly_data, **year2017_monthly_data, **year2018_monthly_data}
all_years_monthly_expenses_str = json.dumps(all_years_monthly_expenses)

with open('years_monthly_expenses.json', 'a') as years_monthly_expenses:
    years_monthly_expenses.write(all_years_monthly_expenses_str)
