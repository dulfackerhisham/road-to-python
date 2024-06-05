"""1) Base levels"""
# passing function as a argument

def subtract(a, b):
    return a - b

def calculate(func, x, y):
    return func(x, y)

print(calculate(subtract, 10, 4))

"""2) Base level"""

def greet_morning(abc):
    def greet_midnight():
        return "good nyt", abc , "sleep well"
    return greet_midnight

greet = greet_morning("lff")
print(greet())
print('------------------------------------------------')

# """decorator"""
# """A Python decorator is a function that takes in a function as argument and returns it by adding some functionality, without changing the structure of original function"""
#case 1
def decorator(func):
    print('im decorator function')
    def inner_dec():
        print('here we add aditional functionality')

        func()

    return inner_dec

@decorator
def original_func():
    print('im original function')


original_func()
print('================================================')

# #Case 2
def dec_divide(func):
    def inner_div(a, b):
        print(f"{a} and {b} is going to divide")
        if b == 0 or a == 0:
            print('cant divide with 0 sorry')
            return
        return func(a,b)
    return inner_div

@dec_divide
def divide(a,b):
    return a/b #or just print

print(divide(6, 9))

divide(0, 4)

# #case 3
def hello(func):
    def inner(*args, **kwargs):
        print("$" * 10)
        func(*args, **kwargs)
        print("$" * 10)
    return inner

def hey(func):
    def inner(*args, **kwargs):
        print("@" * 10)
        func(*args, **kwargs)
        print("@" * 10)
    return inner

@hello
@hey
def og(msg):
    print("hey there")

og('yoo')



