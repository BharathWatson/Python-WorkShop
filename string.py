a="abcdef12345"
sum=0
for i in a:
    if i.isdigit()==True:
        sum+=int(i)
print("sum :",sum)