password = input("Enter password: ")

while password != "pass123":
    if password == "pass123":
        print("Correct")
    else:
        print("Try again")
        password = input("Enter password: ")