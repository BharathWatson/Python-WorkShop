names=[]
emails=[]
n=int(input("enter a number : "))
for i in range(n):
    print("enter no:{} details ****".format(i+1))
    names.append(str(input("enter your name : ")))
    emails.append(str(input("enter your email : ")))
print("List of names : ",names)
print("List of EMAILS : ",emails)