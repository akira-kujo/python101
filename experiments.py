user_prompt = "Enter a todo:"
todos = []

# only put in while loop what you want repeated
while True:
    todo = input(user_prompt)
    print(todo.capitalize())
    todos.append(todo)
