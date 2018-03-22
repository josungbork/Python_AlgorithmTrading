import win32com.client

excel = win32com.client.Dispatch("Excel.Application")
excel.Visible = True
wb = excel.workbooks.Add()
ws = wb.Worksheets("Sheet1")
ws.Cells(1,1).Value = "hello world"
wb.SaveAs('C:\\Users\\khs88\\Desktop\\test.xlsx')
excel.Quit()