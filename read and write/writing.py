file = open("newfile.txt", "w")  # writing in write mode
file.writelines(["Line1\n", "Line2\n"])  # writing a list to a file
file.close()

file = open("newfile2.txt", "w")
file.write('Hey this is just text here and there. You can provide \n characters here as well')
file.close()

file = open("newfile2.txt", "r")  # open the file in readmode
file.read()  # readlines would be for reading a list, read is for a string
file.close()
