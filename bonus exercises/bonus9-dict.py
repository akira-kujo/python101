password = input("Enter new password: ")
result = {}

if len(password) >= 8:
    result['length'] = True  # length is key and True / False is value
else:
    result['length'] = False

digit = False # value of digit is false
for i in password:
    if i.isdigit(): # If password contains number
        digit = True # value of digit becomes true

result['digits'] = digit # digit var becomes value for the 'digits' key

uppercase = False
for i in password:
    if i.isupper():
        uppercase = True

result['upper'] = uppercase

print(result)

if all(result.values()): # if the VALUES of the dict are not ALL TRUE dont print True
    print("Strong password")
else:
    print("Weak password")
