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

def has_year_in_title(sheet):
    return sheet.title.find('201') == 0

def is_expense(cell):
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

def calculate_average_foodoutside(year_category_cells):
    year_category_expenses = list(find_category_expenses(year_category_cells))
    year_foodoutside_list_int = convert_str_to_int(year_category_expenses)
    return find_average_amount(year_foodoutside_list_int)

# list foodoutside expenses for 2013
# year_2013_worksheet = nzfees_worksheet.worksheet("2013")
# year_2013_cells = []
#
# create_expenses_array(5, year_2013_cells, year_2013_worksheet)
#
# year_2013_category_expenses = list(find_category_expenses(year_2013_cells))
#
# year_2013_foodoutside_list_int = convert_str_to_int(year_2013_category_expenses)
#
# # -1 because started from February
# year_2013_foodoutside = sum(year_2013_foodoutside_list_int)/(len(year_2013_foodoutside_list_int) - 1)
#
# pp.pprint('year_2013_foodoutside ' + str(year_2013_foodoutside))
#
# # list foodoutside expenses for 2014
#
# year_2014_worksheet = nzfees_worksheet.worksheet("2014")
# year_2014_cells = []
#
# create_expenses_array(5, year_2014_cells, year_2014_worksheet)
# year_2014_foodoutside = calculate_average_foodoutside(year_2014_cells)
#
# pp.pprint('year_2014_foodoutside ' + str(year_2014_foodoutside))

# list foodoutside expenses for 2015
#
# year_2015_worksheet = nzfees_worksheet.worksheet("2015")
# year_2015_cells = []
#
# create_expenses_array(5, year_2015_cells, year_2015_worksheet)
# year_2015_foodoutside = calculate_average_foodoutside(year_2015_cells)
#
# pp.pprint('year_2015_foodoutside ' + str(year_2015_foodoutside))
#
# # list foodoutside expenses for 2016
#
# year_2016_worksheet = nzfees_worksheet.worksheet("2016")
# year_2016_cells = []
#
# create_expenses_array(5, year_2016_cells, year_2016_worksheet)
# year_2016_foodoutside = calculate_average_foodoutside(year_2016_cells)
#
# pp.pprint('year_2016_foodoutside ' + str(year_2016_foodoutside))
#
# list foodoutside expenses for 2017
#
# year_2017_worksheet = nzfees_worksheet.worksheet("2017")
# year_2017_cells = []
#
# create_expenses_array(5, year_2017_cells, year_2017_worksheet)
# year_2017_foodoutside = calculate_average_foodoutside(year_2017_cells)
#
# pp.pprint('year_2017_foodoutside ' + str(year_2017_foodoutside))
#
# # list foodoutside expenses for 2018
#
# year_2018_worksheet = nzfees_worksheet.worksheet("2018")
# year_2018_cells = []
#
# create_expenses_array(5, year_2018_cells, year_2018_worksheet)
# year_2018_foodoutside = calculate_average_foodoutside(year_2018_cells)
#
# pp.pprint('year_2018_foodoutside ' + str(year_2018_foodoutside))

year_2013_foodoutside_average = 35.09
year_2014_foodoutside_average = 128.5
year_2015_foodoutside_average = 117.7
year_2016_foodoutside_average = 80.16
year_2017_foodoutside_average = 140.58
year_2018_foodoutside_average = 151.66

year_2013_foodoutside_total =
year_2014_foodoutside_total =
year_2015_foodoutside_total = 
year_2016_foodoutside_total =
year_2017_foodoutside_total =
year_2018_foodoutside_total =

foodoutside_average_list = [year_2013_foodoutside_average, year_2014_foodoutside_average, year_2015_foodoutside_average, year_2016_foodoutside_average, year_2017_foodoutside_average, year_2018_foodoutside_average]
foodoutside_total_list = [year_2013_foodoutside_total, year_2014_foodoutside_total, year_2015_foodoutside_total, year_2016_foodoutside_total, year_2017_foodoutside_total, year_2018_foodoutside_total]

all_years_foodoutside_average_object = {}
i = 0
while (i < len(all_years_list)):
    all_years_foodoutside_average_object[all_years_list[i]] = foodoutside_average_list[i]
    i += 1

all_years_foodoutside_total_object = {}
i = 0
while (i < len(all_years_list)):
    all_years_foodoutside_total_object[all_years_list[i]] = foodoutside_total_list[i]
    i += 1

# put foodoutside expenses into json
foodoutside = {}
foodoutside['foodoutside_average'] = all_years_foodoutside_average_object
foodoutside['foodoutside_total'] = all_years_foodoutside_total_object
all_years_foodoutside_str = json.dumps(foodoutside)

with open('data_foodoutside_expenses.json', 'a') as data_foodoutside_expenses:
    data_foodoutside_expenses.write(all_years_foodoutside_str)
