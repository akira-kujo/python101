# with open("file.txt", 'r') as file:
#     content = (file.read())
#     print(content)
#     print(len(content))

with open('name.txt', "r") as file:
    content = file.readlines() # returns as separate strings in a list
    content2 = file.read() # returns text as single string

    print(content)
    print(content2)
