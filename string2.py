a='''the most important 9857907
THE TAJH JUNI THEIR EXITsrs
the modutuhuf impo9878rtaant
urhkvjrbkrj785895UKBHBUKJVHU
kuhjicnjvjvnjfn jnjn nnjkjii'''
n=0
b=0
c=0
d=0
e=0
vowels=0
for i in a:
    if i.isdigit():
        n+=1
    elif i.isupper():
        b+=1
    elif i.islower():
        c+=1
    elif i=='\n':
        e+=1
    else:
        d+=1
print("no.of digits : ",n)
print("no.of lower chars : ",c)
print("no.of upper chars : ",b)
print("no.of words : ",d)
print(" spacebars : ",d)
print("no of lines : ",e+1)
print("string length : ",len(a))
mylist=['a','e','i','o','u','A','E','I','O','U']
for i in a:
    if i in mylist:
        vowels+=1
print("vowels : ",vowels)
print("consonents : ",len(a)-vowels)