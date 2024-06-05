n = int(input("enter a number "))
total = 0

for i in str(n):
    total += int(i) ** len(str(n))

if n == total:
    print(f"{n} is an armstrong number")
else:
    print(f"{n} not an armstrong number")





























































