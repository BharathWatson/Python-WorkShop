l=[]
n=int(input("enter no of elements - "))
for i in range(n):
    l.append(int(input("enter number - ")))
l.sort()
eve=[i for i in l if i%2==0]
odd=[i for i in l if i%2!=0]
print(eve)
print(odd)