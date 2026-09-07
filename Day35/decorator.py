def decorator(function):
    def wrapper():
        print("Welcome!")
        function()
        print("Thank you!")
    return wrapper


@decorator
def sayhello():
    print("Hello, Good Morning")


sayhello()
