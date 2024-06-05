# x = lambda t: t + 10

# print(x(11))

# """map()"""
# def cube(x):
#     return x*x*x

# list1 = [1, 2, 3, 4, 5]

# list_new = list(map(cube, list1))
# print(list_new)

# """filter()"""
# l = [90, -34, 23, 54, -98, -33, 8]

# newl = list(filter(lambda x: x > 0, l))
# print("positive numbers: ", newl)

"""reduce()"""
from functools import reduce
list_1 =[30, 4, 2, 1, 3]

new = reduce(lambda x, y: x + y, list_1)
print(new)