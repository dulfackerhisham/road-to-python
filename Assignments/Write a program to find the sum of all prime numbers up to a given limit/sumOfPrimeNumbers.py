total = 0
def show(n):
    global total
    for i in range(2, n+1):
        prime = True

        for j in range(2, i):
            if i % j == 0:
                prime = False
                break
        if prime == True:
            total += i 
    print("sum of prime number:", total)


while True:
    n = int(input("enter a positive number "))
    if n == 1:
        print(f"{n} is not a prime number,pls try for another number")
    elif n <= 0:
        print(f"{n} is not a prime number,pls enter any positive number")
    else:
        show(n)
        break