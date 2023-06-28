# try:
#     width = float(input("Enter a rectangle width: "))
#     length = float(input("Enter a rectangle length "))
#
#     if width == length:  # if conditionals don't check errors they check values
#         exit("That looks like a square")
#
#     area = width * length
#     print(area)
# except ValueError:
#     print("Incorrect Values, enter a number")

try:
    waiting_list = ["john", "marry"]
    name = input("Enter name: ")

    number = waiting_list.index(name)
    print(f"{name}'s turn is {number}")

except ValueError:
    print("This person is not in the list")


