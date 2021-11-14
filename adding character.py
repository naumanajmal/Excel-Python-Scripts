import pyautogui
import time
import openpyxl as xl
import clipboard
wb = xl.load_workbook('Book12.xlsx')
sheet = wb['Sheet1']
number = 1
for row in range(1, 548):
  cell1 = sheet.cell(row, 1)
  data = str(cell1.value)
  data = "{[[[[[[[[[[[[[[{{[[[[[[[[[[[[[[[[______________________"+str(number)+"_________________]]]]]]]]]]]]]]}}}]]]]]]]]]]]]" +data
  cell1.value = data
  number = number +1


wb.save('Book12.xlsx')

