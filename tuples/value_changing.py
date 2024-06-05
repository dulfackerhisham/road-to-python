x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "hello"
x = tuple(y)
print(x)