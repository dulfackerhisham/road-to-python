"""we use = operator to create a copy of an object. You may think that this creates a new object; it doesn't. 
It only creates a new variable that shares the reference of the original object."""

list1 = [10, 20 , 30 ,'izu']
list2 = list1

print(id(list1))
print(id(list2))