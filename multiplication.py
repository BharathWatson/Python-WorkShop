a=int(input("enter a number - "))
for i in range(1,a+1):
    print("\n",i," table is : -")
    print("--------------------")
    for j in range(1,11):
        print(i," * ",j," = ",i*j)