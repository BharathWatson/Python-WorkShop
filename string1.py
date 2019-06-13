a="abc 123 def 456"
sum=0
for i in a.split():
    if i.isnumeric():
        sum+=int(i)
print("sum : ",sum)