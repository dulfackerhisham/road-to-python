# ab = {4, 6, 10}
# print(ab)

# se = {45, "izu", True, 45.3}
# print(se)

# harry = set()
# print(type(harry))


# for value in se:  #accessing values in a set
#     print(value)

"""SET METHODS => MANIPULATION"""
num_1 = {2, 5, 8, 1}
num_2 = {4, 8, 6, 2, 7}
print(num_1.union(num_2))
num_1.update(num_2)
print(num_1, num_2)