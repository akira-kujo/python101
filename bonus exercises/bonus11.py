def get_average():
    with open("files/data.txt", "r") as file:
        data = file.readlines()

    values = data[1:] # grab the list after temperature
    values = [float(i) for i in values] # list compr make all values a float
    average_local = sum(values) / len(values) # total / amount
    return average_local


average = get_average()
print(average)
