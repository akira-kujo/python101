
while True:
    user_action = input("Type add, show, edit or exit: ")
    user_action = user_action.strip()
    match user_action:
        case 'add':
            todo = input("Enter a to do: ") + "\n"

            file = open('../loops/todos.txt', 'r')  # read the file and NOT overrite previous stuff
            todos = file.readlines()
            file.close()  # close file after usage

            todos.append(todo)  # append the info to the .txt file

            file = open('../loops/todos.txt', 'w')  # allows creating new files or writing new things into the .txt file
            file.writelines(todos)
            file.close()

        case 'show':
            file = open('../loops/todos.txt', 'r')
            todos = file.readlines()
            file.close()

            # new_todos = []
            # for item in todos:
            #     new_item = item.strip('\n')
            #     new_todos.append(new_item) # new items is appended into new_todos

            new_todos = [item.strip('\n') for item in todos] # for item in todos, store item.strip into the new_todos list

            for index, item in enumerate(new_todos):
                row = f"{index + 1}.{item}"
                print(row)

        case 'edit':
            number = int(input("Number of items in todo to edit: "))
            file = open('../loops/todos.txt', 'r')
            todos = file.readlines()
            file.close()

            number = number - 1
            new_todo = input("Enter new to do:") + "\n"
            todos[number] = new_todo

            todos.append(new_todo)

            file = open('../loops/todos.txt', 'w')
            file.writelines(new_todo) # open in write mode, replacing the previous content with the new_todo input
            file.close()

        case 'exit':
            break

print("Bye!")

