"""(*) => asterisk
 there is a situation where we need to pass multiple arguments to the function. Such types of arguments are called arbitrary arguments or variable-length arguments.
 Types of Arbitrary Arguments:

1- arbitrary positional arguments (*`args`)
2- arbitrary keyword arguments (`**kwargs`)"""

#1
def add(*x):
    print(x)
    sum = 0
    for i in x:
        sum = sum + i
    print(sum)

add(5, 6, 20, 55, 20)

#2
def kwarg(**kwargs):
    print(kwargs)

kwarg(name="hisham", age=22, domain="python")
