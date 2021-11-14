hadithnumber = 1
nexthadithno = hadithnumber + 1
hadithnumber = str(hadithnumber)
nexthadithno = str(nexthadithno)
data = "chaptername1hadithtext2hadithtext23"
n = len(hadithnumber)
if hadithnumber in data and not data[:n] == hadithnumber:
    hadithtext = data.partition(hadithnumber)[0]
    data = data.partition(hadithnumber)[2]
    data = hadithnumber + data
    print(hadithtext)
    print(data)