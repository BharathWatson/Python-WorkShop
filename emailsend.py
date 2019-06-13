import smtplib
import getpass
def messege():
    num=int(input("enter number - "))
    names=[]
    emails=[]
    msg=input("enter a messege - ")
    for send in range(num):
        names.append(input("enter name of friend - "))
        emails.append(input("enter email address - "))
    server=smtplib.SMTP("smtp.gmail.com",465)
    server.starttls()   #tls - transport layer security
    server.login("bharathwatson463@gmail.com",getpass.getpass("password - "))
    for mail in emails:
        server.sendmail("bharathwatson463@gmail.com",mail,"hi\n i'm bharath . mail send from python3 smtplib module")
    server.quit()
messege()
