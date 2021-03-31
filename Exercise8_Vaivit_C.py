Username = input("Username : ")
Password = input("Password : ")
if Username == "Host" and Password == "1234":
    print("Welcome, Back!")
    print("--------------------")
    print("1. Apple  30 THB")
    print("2. Orange 25 THB")
    print("3. Tomato 35 THB")
    print("--------------------")
    Goods = int(input("What do you want? (1 or 2 or 3) : "))
    Volume = int(input("How many do you want? : "))
    print("--------------------")
    if Goods == 1:
        print("Apple X", Volume, "=", 30 * Volume, "THB")
    elif Goods == 2:
        print("Orange X", Volume, "=", 25 * Volume, "THB")
    elif Goods == 3:
        print("Tomato X", Volume, "=", 35 * Volume, "THB")
    else:
        print("Error!, We don't have that product.")
        print("Please, try again.")
else:
    print("Wrong!")
    print("Please, try again!")