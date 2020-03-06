user = "root"
pwd = "1234"

if input("user: ") == user and input("pass: ") == pwd:
    print("Login Success")
    print("-"*10," SimplePOS ","-"*10)
    print("1. Item0     10$")
    print("2. Item1     15$")
    print("3. Item2     20$")
    print("4. Item3     25$")
    print("5. Item4     30$")
    userSelected = int(input("\nPlease select what you want to buy.\n:"))

    if userSelected == 1:
        price = 10
    if userSelected == 2:
        price = 15
    if userSelected == 3:
        price = 20
    if userSelected == 4:
        price = 25
    if userSelected == 5:
        price = 30

    '''quantities'''
    quant = int(input("Quantities : "))
    total = price*quant
    print("That's about ",total,"$")