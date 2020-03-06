num = int(input("Enter number: "))
x = num
for i in range(num):
    print(" "*x,"*"*(1+2*i))
    x -= 1