import openpyxl
wb = openpyxl.Workbook()
ws =wb.active
print(ws)
print(wb)
wb.save("test_for_vscode")
