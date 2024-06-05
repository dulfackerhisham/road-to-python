list1 = ["h","el","looo"]
print(id(list1))
list2 = list1
print(id(list2))

list1[1] = 555

print(list1)
print(list2)



list3 = list1.copy()
print(list3)

list3[1] = "aflu"
print(list3)
print(list1)
print(list2)


