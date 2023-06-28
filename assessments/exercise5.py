filenames = ['document', 'report', 'presentation']

for index, item in enumerate(filenames):
    f_string = f"{index}-{item.capitalize()}.txt"
    print(f_string)


# ips = ['100.122.133.105', '100.122.133.111']
#
# len_ips = len(ips) - 1
# desired_index = int(input(f"Enter the index of the IP you want, between 0 and {len_ips}: "))
# message = f"you chose {ips[desired_index]}"
# print(message)
