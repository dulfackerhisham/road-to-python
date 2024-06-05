# removes leading and trailing charecters

"""removing whitespaces"""
string = "                                how's weather    "
print(string)
print(string.strip())

"""removing specific charecters"""
x = "+++++!!!!!t!a!d!a y*o!!!!**+++++"
print(x.strip)
print(x.strip("!"))
"""method to remove multiple charecters"""
print(x.strip("!*+"))


"""removing leading charecters only"""
y = "12345Hello, World12345"
print(y.lstrip("12345"))


"""removing trailing charecters only"""
n = "------Hello, World------"
print(id(n.rstrip("-")))
print(id(n)) #strip returns new string thats y our og string is still there
