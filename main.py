import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pprint

pp = pprint.PrettyPrinter()

scope = ['https://www.googleapis.com/auth/drive.readonly']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(creds)

worksheet = client.open('NZ fees')
worksheet_list = worksheet.worksheets()

def has_year_in_title(sheet):
    return sheet.title.find('201') == 0

def find_fees_worksheets():
    return filter(has_year_in_title, worksheet_list)

filtered_worksheet_list = list(find_fees_worksheets())

# year2017cells = worksheet.worksheet("2017")

result = year2017cells.cell(2,2).value
# pp.pprint(worksheet_list[0].title)
pp.pprint(filtered_worksheet_list)
