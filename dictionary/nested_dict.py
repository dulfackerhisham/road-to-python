my_family = {
    "father": {
        "name": "dulfacker",
        "occupation": "business",
    },

    "mother": {
        "name": "jouhara",
        "occupation": "house wife",
    },

    "child_1": {
        "name": "hisham",
        "occupation": "software engineer",
    },

    "child_2": {
        "name": "nidal",
        "occupation": "student",
    },

    "child_3": {
        "name": "izan",
        "occupation": "student",
    }
}

# for key, value in my_family.items():
#     print(key, value)

"""accessing elements"""
# print(my_family["child_2"]["name"])

"""looping through"""
for i, j in my_family.items():
    print(i)

    for x in j:
        print(f"{x}: {j[x]}")



"""another way"""
# father = {
#         "name": "dulfacker",
#         "occupation": "business",
#     },

# mother = {
#         "name": "jouhara",
#         "occupation": "house wife",
#     },

# child_1 = {
#         "name": "hisham",
#         "occupation": "software engineer",
#     },

# child_2 = {
#         "name": "nidal",
#         "occupation": "student",
#     },

# child_3 = {
#         "name": "izan",
#         "occupation": "student",
#     }

# faaam = {
#     "father": father,
#     "mother": mother,
#     "child_1": child_1,
#     "child_2": child_2,
#     "child_3": child_3,
# }
