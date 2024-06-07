#dict wont allow duplicate keys
my_dict = {
    "name": "hisham",
    "age": 23,
    "place": "koyilandy",
    "born": 2001,
    "year": 2000,
    "born": 2000,
}

# print(my_dict)
# print(my_dict.items())
# print(my_dict.keys())
# print(my_dict.values())

"""length of dict"""
print(len(my_dict))

names = {
    "name": "aflu",
    "boool": True,
    123: "numbers",
    "list": [132, 555],
    "tuple": (777, 888),
    "set": {999, 33, 999}
}
print(names)

"""creating dictionary with dict constructor"""
food = dict(fruit = "mango", price = 55, location = "calicut")
print(food)
