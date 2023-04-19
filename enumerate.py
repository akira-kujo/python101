waiting_list = ["sen", "ben", "john"]
waiting_list.sort()  # lists are mutable so the method of sorting will change the list
# ^ doesn't have to be assigned as a var first
for index, item in enumerate(waiting_list):
    row = f"{index + 1}.{item.capitalize()}"
    print(row)

# enumerate creates objects as tuples when func is used
