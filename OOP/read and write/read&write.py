while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    match user_action:
        case 'add':
            todo = input("Enter a to do: ") + "\n"

            with open('../write & open/todos.txt', 'r') as file: # open file in read mode
                todos = file.readlines()

            todos.append(todo)  # append the info to the .txt file

            with open('../write & open/todos.txt', 'w') as file:  # write into file
                todos = file.writelines(todos)

        case 'show':

            with open('../write & open/todos.txt', 'r') as file:
                todos = file.readlines()

            new_todos = []
            for item in todos:
                new_item = item.strip('\n')
                new_todos.append(new_item) # new items is appended into new_todos

            new_todos = [item.strip('\n') for item in
                         todos]  # for item in todos, store item.strip into the new_todos list

            for index, item in enumerate(new_todos):
                item = item.strip('\n')
                row = f"{index + 1}.{item}"
                print(row)

        case 'edit':
            number = int(input("Number of items in todo to edit: "))
            number = number - 1

            with open('../write & open/todos.txt', 'r') as file:
                todos = file.readlines()

            new_todo = input("Enter new to do: ")
            todos[number] = new_todo + '\n'

            with open('../write & open/todos.txt', 'w') as file:
                todos = file.writelines(todos)

        case 'complete':
            number = int(input("Number of the todos to complete: "))

            with open('../write & open/todos.txt', 'r') as file:
                todos = file.readlines()
            index = number - 1 # pop in index according to number listing
            todo_to_remove = todos[index] # read the index placement in todos.txt
            todos.pop(index) # code to remove it

            with open('../write & open/todos.txt', 'w') as file:
                file.writelines(todos) # write into list and remove it

            message = f"{todo_to_remove} was removed from the list"
            print(message)

            # todos.append(new_todo)
            #
            # file = open('../loops/todos.txt', 'w')
            # file.writelines(new_todo) # open in write mode, replacing the previous content with the new_todo input
            # file.close()

        case 'exit':
            break

print("Bye!")
