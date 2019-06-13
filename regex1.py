import re
l=['sameer','jani','bharath ','12345','chandu ','prassanaraj ','balu','sbalu','bchandra','fry','bcd']
for i in l:
    if re.findall('[a-z0-9]',i):  # ^ , * , . , $ , \s , \S ,'[aeiou]','[0-9]'
        print(i)