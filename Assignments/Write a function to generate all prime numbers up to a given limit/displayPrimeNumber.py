def main():
    while True:
        n = int(input("enter a positive number "))
        if n == 1:
            print(f"there are no prime numbers in between {n}")
        elif n == 0:
            print(f"{n} is not a positive number")
        elif n > 0:
            break
    display(n)

def display(n):
    print("prime numbers are")
    for i in range(2, n+1):
        is_prime = True
        
        for j in range(2, i):
            if i % j == 0:
                is_prime = False
                break
        if is_prime == True:
            print(i)

main()
