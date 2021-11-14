
import clipboard
data = clipboard.paste()
if "_____"  in data:
 hadithtext = data.partition(data)[2]
 print(hadithtext)