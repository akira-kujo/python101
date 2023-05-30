password = input("Enter new password: ")
result = []

if len(password) >= 8:
    result.append(True)
else:
    result.append(False)

digit = False # value of digit is false
for i in password:
    if i.isdigit(): # If password contains number
        digit = True # value of digit becomes true

result.append(digit)  # append digit to the list

uppercase = False
for i in password:
    if i.isupper():
        uppercase = True

result.append(uppercase)

if all(result):
    print("Strong password") # if at least one of params (upper, digits, 8) is false, return false
else:
    print("Weak password")
