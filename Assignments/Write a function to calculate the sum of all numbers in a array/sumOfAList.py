x = int(input("enter list size "))
arr = []

def main(x):
    sum = 0
    print("enter list values ")
    for _ in range(x):
        num = int(input())
        arr.append(num)
        sum += num
    return sum

print(main(x))

# OR

# arr = [6,8,9,40,99]
# total = sum(arr)
# print("sum of elements in a list", total)
