import gspread
from oauth2client.service_account import ServiceAccountCredentials
import json
import re
import pprint

pp = pprint.PrettyPrinter()

# connect to google api and open NZ fees spreadsheet
scope = ['https://www.googleapis.com/auth/drive.readonly']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(creds)

nzfees_worksheet = client.open('NZ fees')
nzfees_worksheet_list = nzfees_worksheet.worksheets()

def has_year_in_title(sheet):
    return sheet.title.find('201') == 0

def find_fees_worksheets():
    return filter(has_year_in_title, nzfees_worksheet_list)

filtered_nzfees_worksheet_list = list(find_fees_worksheets())

all_years_list = []
i = 0
while (i < len(filtered_nzfees_worksheet_list)):
    all_years_list.append(int(filtered_nzfees_worksheet_list[i].title))
    i += 1
all_years_list_in_order = all_years_list[::-1]

def has_year_in_title(sheet):
    return sheet.title.find('201') == 0

def is_expense(cell):
    if type(cell) == str:
        return cell.find('$') == 0

def find_category_expenses(year_cells):
    return filter(is_expense, year_cells)

def create_expenses_array(expense_cell, year_cells, year_worksheet):
    for month_expense_cell in range(2, 36):
        year_cells.append(year_worksheet.cell(expense_cell, month_expense_cell).value)

def convert_str_to_int(old_list):
    new_list = []
    for number in old_list:
        new_list.append(int(re.sub('[$,]', '', number)))
    return new_list

def find_average_amount(expense_list):
    return sum(expense_list)/len(expense_list)

def calculate_average_rent(year_category_cells):
    year_category_expenses = list(find_category_expenses(year_category_cells))
    year_rent_list_int = convert_str_to_int(year_category_expenses)
    return find_average_amount(year_rent_list_int)

def calculate_total_rent(year_category_cells):
    year_category_expenses = list(find_category_expenses(year_category_cells))
    year_rent_list_int = convert_str_to_int(year_category_expenses)
    return sum(year_rent_list_int)

# list rent expenses for 2013
year_2013_worksheet = nzfees_worksheet.worksheet("2013")
year_2013_cells = []

create_expenses_array(2, year_2013_cells, year_2013_worksheet)

year_2013_category_expenses = list(find_category_expenses(year_2013_cells))
year_2013_rent_list_int = convert_str_to_int(year_2013_category_expenses)

# -1 because started from February
year_2013_rent_average = sum(year_2013_rent_list_int)/(len(year_2013_rent_list_int) - 1)
year_2013_rent_total = calculate_total_rent(year_2013_cells)

pp.pprint('year_2013_rent_average ' + str(year_2013_rent_average))
pp.pprint('year_2013_rent_total ' + str(year_2013_rent_total))

# list rent expenses for 2014

year_2014_worksheet = nzfees_worksheet.worksheet("2014")
year_2014_cells = []

create_expenses_array(2, year_2014_cells, year_2014_worksheet)
year_2014_rent_average = calculate_average_rent(year_2014_cells)
year_2014_rent_total = calculate_total_rent(year_2014_cells)

pp.pprint('year_2014_rent_average ' + str(year_2014_rent_average))
pp.pprint('year_2014_rent_total ' + str(year_2014_rent_total))

# list rent expenses for 2015

year_2015_worksheet = nzfees_worksheet.worksheet("2015")
year_2015_cells = []

create_expenses_array(2, year_2015_cells, year_2015_worksheet)
year_2015_rent_average = calculate_average_rent(year_2015_cells)
year_2015_rent_total = calculate_total_rent(year_2015_cells)

pp.pprint('year_2015_rent_average ' + str(year_2015_rent_average))
pp.pprint('year_2015_rent_total ' + str(year_2015_rent_total))

# list rent expenses for 2016

year_2016_worksheet = nzfees_worksheet.worksheet("2016")
year_2016_cells = []

create_expenses_array(2, year_2016_cells, year_2016_worksheet)
year_2016_rent_average = calculate_average_rent(year_2016_cells)
year_2016_rent_total = calculate_total_rent(year_2016_cells)

pp.pprint('year_2016_rent_average ' + str(year_2016_rent_average))
pp.pprint('year_2016_rent_total ' + str(year_2016_rent_total))

# list rent expenses for 2017

year_2017_worksheet = nzfees_worksheet.worksheet("2017")
year_2017_cells = []

create_expenses_array(2, year_2017_cells, year_2017_worksheet)
year_2017_rent_average = calculate_average_rent(year_2017_cells)
year_2017_rent_total = calculate_total_rent(year_2017_cells)

pp.pprint('year_2017_rent_average ' + str(year_2017_rent_average))
pp.pprint('year_2017_rent_total ' + str(year_2017_rent_total))

# list rent expenses for 2018

year_2018_worksheet = nzfees_worksheet.worksheet("2018")
year_2018_cells = []

create_expenses_array(2, year_2018_cells, year_2018_worksheet)
year_2018_rent_average = calculate_average_rent(year_2018_cells)
year_2018_rent_total = calculate_total_rent(year_2018_cells)

pp.pprint('year_2018_rent_average ' + str(year_2018_rent_average))
pp.pprint('year_2018_rent_total ' + str(year_2018_rent_total))

def list_category_expenses(year, category_cell_num, year_cells):
    year_worksheet = nzfees_worksheet.worksheet(year)

    create_expenses_array(category_cell_num, year_cells, year_worksheet)
    year_category_average = calculate_average_rent(year_cells)
    year_category_total = calculate_total_rent(year_cells)
    result = {year['average']: year_category_average, year['total']: year_category_total}
    return result

# merge expenses into one object

rent_list_average = [year_2013_rent_average, year_2014_rent_average, year_2015_rent_average, year_2016_rent_average, year_2017_rent_average, year_2018_rent_average]
rent_list_total = [year_2013_rent_total, year_2014_rent_total, year_2015_rent_total, year_2016_rent_total, year_2017_rent_total, year_2018_rent_total]

rent_list_average = [year_2015_rent_average, year_2016_rent_average]
rent_list_total = [year_2015_rent_total, year_2015_rent_total]
all_years_rent_average = {}
all_years_rent_total = {}

a = 0
while (a < len(all_years_list_in_order)):
    all_years_rent_average[all_years_list_in_order[a]] = rent_list_average[a]
    a += 1

t = 0
while (t < len(all_years_list_in_order)):
    all_years_rent_total[all_years_list_in_order[t]] = rent_list_total[t]
    t += 1

pp.pprint(all_years_rent_total)
pp.pprint(all_years_rent_average)

# put rent expenses into json
rent = {
    'rent': {
        'rent_total': all_years_rent_total,
        'rent_average':  all_years_rent_average
        }
    }
pp.pprint(rent)
all_years_rent_str = json.dumps(rent)

with open('data_rent_expenses.json', 'a') as data_rent_expenses:
    data_rent_expenses.write(all_years_rent_str)
