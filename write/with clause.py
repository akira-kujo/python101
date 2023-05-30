with open("../write/doc.txt", "r") as file:
    file.read() # if read() called twice will show blank as it goes to end of file to read again (which = blank)
    content = file.read()
    print(content)



