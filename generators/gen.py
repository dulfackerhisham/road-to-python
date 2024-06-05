def my_generator():

    yield 5

val = my_generator()
print(next(val))


def add(num):
    for i in num:
        yield i

my_num = add([5,6,9])

print(my_num)
print(next(my_num))
print(next(my_num))
print(next(my_num))