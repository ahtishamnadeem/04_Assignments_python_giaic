# Decorator function that logs function call
def log_function_call(func):
    def wrapper():
        print("Function is being called")
        return func()  # Calls the original function
    return wrapper

# Function to say hello
@log_function_call
def say_hello():
    print("Hello, world!")

# Calling the function
say_hello()
