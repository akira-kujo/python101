password = input("Enter a new password: ")

while len(password) < 7:
    print("Not a good password, try again")
    password = input("Enter a new password: ")
if len(password) == 7:
    print("Password is OK, but not too strong")
    password = input("Enter a new password: ")
else:
    pass

print("Great Password!")

