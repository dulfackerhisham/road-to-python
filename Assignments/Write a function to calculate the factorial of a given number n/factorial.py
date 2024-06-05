def main():
    while True:
        n = int(input("enter a number "))
        if n == 0:
            print(f"factorial of {n} = 1")
        elif n > 0:
            result = display(n)
            print(f"factorial of {n} = {result}")

def display(n):
    summ = 1
    for i in range(1, n+1):
        summ = summ * i
    return summ

main()