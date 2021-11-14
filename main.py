import pyautogui
import openpyxl as xl
import clipboard
wb = xl.load_workbook('')
sheet = wb['Sheet1']
cell = sheet['a1']
celldata = cell.value
celldata = str(celldata)

pyautogui.hotkey('ctrl', 'v')
text = clipboard.paste()