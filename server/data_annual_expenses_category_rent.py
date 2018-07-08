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
    all_years_list.append(filtered_nzfees_worksheet_list[i].title)
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

def calculate_average_for_category(year_category_cells):
    year_category_expenses = list(find_category_expenses(year_category_cells))
    year_category_list_int = convert_str_to_int(year_category_expenses)
    return find_average_amount(year_category_list_int)

def calculate_total_for_category(year_category_cells):
    year_category_expenses = list(find_category_expenses(year_category_cells))
    year_category_list_int = convert_str_to_int(year_category_expenses)
    return sum(year_category_list_int)

def list_category_expenses(year, category_cell_num, year_cells):
    year_worksheet = nzfees_worksheet.worksheet(year)
    create_expenses_array(category_cell_num, year_cells, year_worksheet)
    year_category_average = calculate_average_for_category(year_cells)
    year_category_total = calculate_total_for_category(year_cells)
    result = {
        year: {
            'average': year_category_average,
            'total': year_category_total
        }
    }
    return result

def get_category_expenses (cell):
    result = []
    a = 0
    while (a < len(all_years_list_in_order)):
        this_year = list_category_expenses(all_years_list_in_order[a], cell, [])
        result.append(this_year)
        a += 1
    return result

rent = list(get_category_expenses(2))
food_home = list(get_category_expenses(4))
food_outside = list(get_category_expenses(5))
home_facilities = list(get_category_expenses(6))
wellbeing = list(get_category_expenses(9))
sport = list(get_category_expenses(11))
car = list(get_category_expenses(13))

all_categories_object = {
    'rent': rent,
    'food_home': food_home,
    'food_outside': food_outside,
    'home_facilities': home_facilities,
    'wellbeing': wellbeing,
    'sport': sport,
    'car': car
}

all_categories_annual_str = json.dumps(all_categories_object)

with open('data_categories_expenses.json', 'a') as data_categories_expenses:
    data_categories_expenses.write(all_categories_annual_str)
