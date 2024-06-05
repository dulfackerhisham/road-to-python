n = int(input("enter a number "))
sum = 0

while True:
    odd_even = int(input("enter 1 for Even numbers & 2 for Odd numbers "))
    if odd_even == 1 or odd_even ==2:
        break
    else:
        print("please choose number 1 or 2 ")

for i in range(1, n):
    if odd_even == 1:
        if i % 2 == 0:
            sum += i
    elif odd_even == 2:
        if i % 2 != 0:
            sum += i

print(f"{sum}")
