import pyautogui
import time
import openpyxl as xl
import clipboard
wb = xl.load_workbook('Book1.xlsx')
sheet = wb['Sheet1']
number = 1
for row in range(1, 548):
  cell1 = sheet.cell(row, 1)
  data = str(cell1.value)
  print(data)
  data1 = data.replace(data[:7], '')
  #g = 1
  #for i in data:
      #if i =="[" or "]" or "{" or "}" or " " or "(" or ")" or  "1" or "2" or "3" or "4" or "5" or "6" or "7" or "8" or "9" or "0" or "_":
         # data = data.replace(i, "")
         # print(i)
         # g = g+1
         # if g ==500:
          #    break
  cell1.value = data1



wb.save('Book1.xlsx')

