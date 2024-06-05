
# x = int(input("enter a number which is multiple of 3 or 5"))

# def display(n):
#     if (n % 3 ==0) and (n % 5 == 0):
#         print("ab")
#     elif n % 3 == 0:
#         print("a")
#     elif n % 5 == 0:
#         print("b")
#     else:
#         print("entered number is not multiple of 3 & 5")

def show(func):
    def inner():
        func()
    return inner
#closure property =>


@show
def greet(name):
    print('hey', name)

greet("hisham")
