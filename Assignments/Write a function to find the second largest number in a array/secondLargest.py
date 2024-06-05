arr = []

def main():
    n = int(input("enter the size of lists "))
    print("enter your lists value ")
    for _ in range(n):
        num = int(input())
        arr.append(num)

    print("second largest no:", secLargest())

def secLargest():
    firstL = 0 #use min method
    secL = 0
    
    for x in arr:
        if x > firstL:
            secL = firstL
            firstL = x
        elif (x < firstL & x > secL):
            secL = x
    return secL

main()

# using set() & remove ()

# list1 = [11,5,80,31,5,4,72]

# new_list = set(list1)  #to get unique elements

# new_list.remove(max(new_list)) #removing the larget element

# print(max(new_list)) #prints the second largest numbr