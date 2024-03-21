import pandas as pd
from openpyxl import Workbook
from openpyxl.utils.dataframe import dataframe_to_rows
from win32com.client import Dispatch

data = {
    "Asset Name": ["Assets 1", "Assets 2"],
    "Month 1":[15,30],
    "Month 2 ":[5,35]
}
df = pd.DataFrame(data)

workbook = Workbook()
sheet = workbook.activate

for row in dataframe_to_rows(df , index=False, header=True):
    sheet.append(row)

workbook.save("pandas.xlsx")
x1 = Dispatch("Excel.Application")
x1.Visible = True
wb = x1.workbooks.Open(r'path')
wb.Close()
x1.Quite()