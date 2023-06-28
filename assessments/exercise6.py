# file = open("essay.txt", "r")
# content = file.read()
# print(content.title())

# file_read = open("essay.txt", "r")
# content = file_read.read()
# file = "essay.txt"
# print(f"the number of characters in {file} is")
# print(len(content))


enter_name = input("please enter a new member: ") + "\n" # grab item / name from user
file_read = open("members.txt", "r") # open the file in read mode
members_list = file_read.readlines()  # read the content of the file members.txt and create a list
print(members_list)
#
#
members_list.append(enter_name) # add the items from input (enter_name) into the list (members_list) and save it


file_write = open("members.txt", "w") # this will overwrite and create a new file
file_write.writelines(members_list) # the contents of this file will have the contents of the list
file_write.close()
print("The new list is:")
print(members_list)

# text_file1 = open("a.txt", "b.txt" "r")
# text_file2 = open("b.txt", "r")
# text_file3 = open("c.txt", "r")
# file_list = (text_file1.readlines())
# print(file_list)

# filenames = ["a.txt", "b.txt", "c.txt"] # make the files into a list
#
# for filename in filenames:
#     file_read = open(filename, "r") # open the files in read list
#     file_listing = file_read.readlines() # read as a list
#     print(file_listing) # print out the file as a list alongside its contents
#
# filelist = ["document.txt", "worddoc.txt", "something.txt"] # write the files into a list
#
# for filename in filelist:  # iterate over the file list
#     file_iterate = open(filename, "w") # open the list in write mode
#     file_iterate.write("hello") # write "hello" into the list
#     file_iterate.close() # close the list

# When opening file in read mode the cursor begins from line 1
# When you apply file.read the cursor reads the text and cursor is at end of line of final text
# If you do file.read() again then it will provide a blank line because its at the end of the line


# file = open("data.txt", 'w')
#
# file.write("100.12\n") # have it written on new line
# file.write("111.23\n")
# file.close()

file = open("data.txt", 'w')
file.write("100.12")
file.close()