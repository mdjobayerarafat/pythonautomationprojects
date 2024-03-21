from openpyxl import Workbook
from win32com.client import Diapatch

workbook = Workbook()
sheet = workbook.activate

sheet["A1"] = "hello"
sheet["B1"] = "Youtube"

workbook.save(filename="hello_youtube.xlsx")
cell = sheet["A1"]
cell.value = "Greetings"
#print(cell.value)

workbook.save(filename="hello_youtube.xlsx")


x1 = Diapatch("Excel.Application")
x1.Visible = True
wb = x1.Workbooks.Open(r'xlsx path')
