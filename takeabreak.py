import time,webbrowser
count=1
breaks=3
print("current time : ",time.ctime())
for i in range(count,breaks+1):
    time.sleep(2)
    if i==1:
        webbrowser.open("www.google.com")
    elif i==2:
        webbrowser.open("www.python.org")
    elif i==3:
        webbrowser.open("www.udemy.com")
    else:
        print("**************")