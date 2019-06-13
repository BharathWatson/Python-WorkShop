a=int(input("enter a integer : "))
b=int(input("enter a integer : "))
print("(1)+\t(2)-\t(3)/\t(4)*\t(5)%\n")
c=int(input("enter your choice"))
if c==1:
    print(a+b)
elif c==2:
    print(a-b)
elif c==3:
    print(a/b)
elif c==4:
    print(a*b)
else:
    print(a%b)