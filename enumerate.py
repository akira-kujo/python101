# waiting_list = ["sen", "ben", "john"]
# waiting_list.sort()  # lists are mutable so the method of sorting will change the list
# # ^ doesn't have to be assigned as a var first
# for index, item in enumerate(waiting_list):
#     row = f"{index + 1}.{item.capitalize()}"
#     print(row)

# enumerate creates objects as tuples when func is used
# tuples store items / values into variables

waiting_list2 = ["akira", "arthur", "annie", "abigail"]
waiting_list2.sort()
for index, item in enumerate(waiting_list2):
    row = f"{index + 1}.{item.capitalize()}"
    print(row)