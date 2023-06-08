def greet():
    message = "hello" # local function
    new_message = message.capitalize() # local function
    print("Hey")
    return new_message # return func ensures that when message var is called as below it appears
    # without return statement function returns a None

greeting = greet() # can call the function, but can't call content inside function (i.e. greeting ≠ new_message)
print(greeting) # the variable ^ for the function simply has to exist for content ("Hey") to be called
