todos = []

while True:
    user_action = input("Type add, show, edit or exit: ")
    user_action = user_action.strip() # if add has trailing space then its stripped
    match user_action:
        case 'add':  # if value of the variable == 'add'
            todo = input("Enter a to do: ")  # do this input
            todos.append(todo)
        case 'show' | 'display':  # if its 'show' or 'display', then print list
            for index, item in enumerate(todos):  # enumerate func allows listing of item place
                new_var = f"{index + 1}.{item}"  # f string literal
                print(new_var)
        case 'edit':
            number = int(input("Number of items in todo to edit: "))  # accepts an int value
            number = number - 1  # for users who aren't aware of python num system
            new_todo = input("Enter new to do:")  # change item in todo list
            todos[number] = new_todo  # item from prev input appends where you chose
        case 'complete':
            number = int(input("Number of items in todo to remove: "))
            todos.pop(number - 1)  # remove the integer corresponding to index that you want
        case 'exit':
            break
        case _:  # a case where it doesn't match
            print("Incorrect command, try again")

print("Bye!")
