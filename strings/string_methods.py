#str's first letter to Caps
x = "dagabazare"
# print(x.capitalize())

#str into lowercase ||||| casefold=> converts to lower cases ascii and non ascii also(special charecters)
y = "ADD&&**ß"
# print(y.casefold())

# print(y.lower())

# centering and no. of times a string appeared in a string
q = "malayalam"
# print(q.count("a", 2, 5))
# print(q.center(20, '!'))

e = "i was good once"
print(e.encode())


r = "this too shall pass"
print(r.endswith("s"))


#returns the position and index of the values
i = "things are gonna change"
print(i.find("ge"))
print(i.index("gon"))
