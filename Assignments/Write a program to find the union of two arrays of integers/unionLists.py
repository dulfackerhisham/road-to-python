arr_1 = []
arr_2 = []

n_1 = int(input("enter the limit of 1st lists "))
n_2 = int(input("enter the limit of 2nd lists "))

for i in range(max(n_1, n_2)):
    if i < n_1:
        val_1 = int(input("enter value for lists-1 "))
        arr_1.append(val_1)
    if i < n_2:
        val_2 = int(input("enter values for lists-2 "))
        arr_2.append(val_2)

def unique(arrr):
    unionList = set(arrr)

    uL = list(unionList)
    return uL

print("union of lists 1", unique(arr_1))
print("union of lists 2", unique(arr_2))