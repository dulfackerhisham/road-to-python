arr = []

def main():
    n = int(input("enter the size of the lists "))
    print("enter your array values \n")
    for _ in range(n):
        num = int(input())
        arr.append(num)

    print("the maximum element in a list:", max_num())

def max_num():
    value = 0
    for i in arr:
        if i > value:
            value = i
    return value

main()

# using max function
