# enumerate creates objects as tuples when func is used
# tuples store items / values into variables

# Enumerate makes sure that the values (index, item) can be used for the element and index of that element

waiting_list2 = ["akira", "arthur", "annie", "abigail"]
waiting_list2.sort()
for index, item in enumerate(waiting_list2):
    row = f"{index + 1}.{item.capitalize()}"
    print(row)