def main():
    n = int(input("enter a number "))
    print("sum = ", total(n))

def total(num):
    sum = 0
    for i in range(num):
        if i % 2 == 0:
            sum += i
    return sum

main()

# try to do with while loop

# n = 10
# sum =0
# i = 0

# while i < n:
#     if i % 2 == 0:
#         sum += i
#     i += 1

# print(sum)
