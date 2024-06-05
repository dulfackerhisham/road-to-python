sum = 0
n = int(input("enter the limit : "))

while True:
    num = int(input("enter number 3 or 5 : "))
    if num == 3 or num == 5:
        break
    else:
        print("please enter number 3 or 5 : ")

for i in range(1, n+1):
    if i % num == 0:
        sum += i

print(sum)