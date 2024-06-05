def main():
    x = int(input("enter a number to check if its prime number "))
    prime(x)

def prime(x):
    if x > 1:
        for i in range(2, x):
            if (x % i) == 0:
                print(f"{x} not a prime number")
                break
        else:
            print(f"{x} is a prime number ")
    else:
        print(f"{x} is not a prime number")
 
main()
