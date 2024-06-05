import copy
arr = ["hello", [33, 22, 44], [99, 75, 84], [63, 57, 82]]
new_arr = copy.deepcopy(arr)

arr.append([55, 55, 55])
print(arr)

new_arr.append([33, 33, 33])
print(new_arr)


print(id(arr))
print(id(new_arr))
print(arr)
print(new_arr)

arr[1][1] = 'BB'
print(arr)
print(new_arr)