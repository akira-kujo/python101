todos = []

while True:
    user_action = input("Type add, show or exit: ")

    match user_action:
        case 'add':  # if value of the variable == 'add'
            todo = input("Enter a to do: ")  # do this input
            todos.append(todo)
        case 'show':  # if its 'show', then print list
            print(todos)
        case 'exit':
            break

print("Bye!")