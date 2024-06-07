names = {'hisham', 'dulfacker', 'liya', 'filsor'}

# print(names)

names.add("fathima")
# print(names)

name_1 = {"izu", "nidal"}

names.update(name_1)
# print(names)

"""adding another iterable python object"""
my_list = [123,465,789]
my_dic = {"number": 123,
          "faa": "foo"
          }

names.update(my_list)
# print(names)

names.update(my_dic)
# print(names)

