limit = int(input("enter a number "))
prev = 0
curr = 1

#printing the 1st number
print(prev)

for i in range(limit - 1):
    #printing the current number
    print(curr)


    #calculating the next number in the series
    nex = prev + curr

    # updating prev and curr
    prev = curr
    curr = nex 
