a=int(input("enter a number : "))
b=int(input("enter a number : "))
c=int(input("enter a number : "))
if a!=b and b!=c:
    print(a+b+c)
elif a==b==c:
    print(0)
else:
    if a==b:
        print(c)
    elif b==c:
        print(a)
    else:
        print(b)
