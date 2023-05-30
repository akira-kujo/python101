# new_todos = []
# for item in todos:
#     new_item = item.strip('\n')
#     new_todos.append(new_item) # new items is appended into new_todos

# new_todos = [item.strip('\n') for item in todos]

# names = ["john smith", "jay santi", "eva kuki"]
#
# new_names = [name.title() for name in names]
# print(new_names)

# usernames = ["john 1990", "alberta1970", "magnola2000"]
# user_numbers = [len(name) for name in usernames]
#
# print(user_numbers)

# user_entries = ['10', '19.1', '20']
#
# user_floats = [float(numbers) for numbers in user_entries]
# print(sum(user_floats))

temperatures = [10, 12, 14]

# temperatures = [str(i) + '\n' for i in temperatures]

# new_temps = []
# for item in temperatures:
#     str_item = str(item) + "\n"
#     new_temps.append(str_item)
#
#
# file = open("file.txt", 'w')
# file.writelines(new_temps)


numbers = [10.1, 12.3, 14.7]

numbers_list = [int(number) for number in numbers]
print(numbers_list)
