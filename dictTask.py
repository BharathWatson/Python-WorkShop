d={'one':1,'two':2,'three':3,'four':4,'five':5}
print(d)
s={}
s.update(d)
for key in s.keys():
    if s[key]%2!=0:
        s[key]=s[key]**2
print(s)