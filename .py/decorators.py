# def print_msg(message):
#     greeting = "Hello"

#     def printer():
#         print(greeting, message)

#     return printer

# func = print_msg("python is awsome")
# func()

def greet(func):
    def inner():
        print("good morning")
        func()
        print("thanks for using this function")
    return inner

@greet
def hello():
    print("hello world")


hello()