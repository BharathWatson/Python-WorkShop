file=open('taskdemo.txt','a')
n=int(input("enter no.of members - "))
for i in range(n):
    file.write('\n')
    file.write(input("enter name - ")+'\t'+input('enter branch - ')+'\t'+input("enter email - ")+'\t')
file.close()
print("written data to the FILE")
file=open('taskdemo.txt','r')
for data in file:
    print(data)
