
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

            for index, item in enumerate(todos):
                new_var = f"{index + 1}.{item}"
                print(new_var)
        case 'edit':
            number = int(input("Number of items in todo to edit: "))
            number = number - 1
            new_todo = input("Enter new to do:")
            todos[number] = new_todo
        case 'exit':
            break

print("Bye!")

