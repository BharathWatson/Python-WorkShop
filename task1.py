import re
names=[]
emails=[]
n=["bharath","bharath@gmail.com",'sravan','sravan@gmail.com','jk','jkidly@gmail.com']
for i in n:
    if re.match('^[a-z0-9]\S.*@\S.*com|in$',i):
        emails.append(i)
    else:
        names.append(i)
print(names,emails)