def star(n):
    return "* "*n

for i in range(6):
    for j in range(6):
        if i<=j:
            print(star(j)+" ")
            break
for i in range(6):
    for j in range(6):
        if j<=i:
            print(star(5-i))
            break