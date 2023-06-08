def get_todos(): # the function
    with open('../write & open/todos.txt', 'r') as file_local:
        todos_local = file_local.readlines() # local variable hold the list
    return todos_local

while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    if user_action.startswith('add'):
        todo = user_action[4:]  # list slicing operation

        todos = get_todos() # grab the list from within the function (todos_local)

        todos.append(todo + '\n') # the list (of things) is then added to the ACTUAL list

        with open('../write & open/todos.txt', 'w') as file:
            todos = file.writelines(todos)

    elif user_action.startswith('show'):

        todos = get_todos()

        new_todos = []
        for item in todos:
            new_item = item.strip('\n')
            new_todos.append(new_item)

        new_todos = [item.strip('\n') for item in
                     todos]
        for index, item in enumerate(new_todos):
            item = item.strip('\n')
            row = f"{index + 1}.{item}"
            print(row)

    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])
            number = number - 1

            todos = get_todos()

            new_todo = input("Enter new to do: ")
            todos[number] = new_todo + '\n'

            with open('../write & open/todos.txt', 'w') as file:
                todos = file.writelines(todos)
        except ValueError: # If there is a ValueError
            print("Your command is not valid.")
            continue

    elif 'complete' in user_action:
        try:
            number = int(user_action[9:])

            todos = get_todos()

            index = number - 1
            todo_to_remove = todos[index]
            todos.pop(index)

            with open('../write & open/todos.txt', 'w') as file:
                file.writelines(todos) # write into list and remove it

            message = f"{todo_to_remove} was removed from the list"
            print(message)
        except IndexError:
            print("There is no item with that number. ")
            continue # if the user enters number not in range then do loop again

    elif 'exit' in user_action:
        break

    else:
        print("try again")

print("Bye!")
