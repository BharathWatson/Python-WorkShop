import re
l=['sameer','jani','bharath','chandu','prassanaraj','balu','sbalu'.'bchandra']
for i in l:
    if (re.findall('s',i)):  # match , search , findall
        print(i)