import re
str1='''the following are the phone numbers of the avengers
iron man - 9848034567
tony stark - 9898989989
captain - 000098009'''
for i in str1:
    if re.match('^[789]\d{9}$',str1):
        print(i)