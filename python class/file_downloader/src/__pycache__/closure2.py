def outer_function(message):
    #value of message is present here
    def inner_function():
        print(message)

    return inner_function

closure=outer_function("Hello from closure")

closure()