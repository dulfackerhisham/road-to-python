fruits = ("apple", "banana", "grape")

(red, yellow, green) = fruits
print(red)
print(type(red))


m = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = m

print(green)
print(yellow)
print(red)