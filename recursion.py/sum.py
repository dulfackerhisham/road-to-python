def sum(n):
    if n == 1:
        return 1
    else:
        return n + sum(n-1)
    
res = sum(10)
print(res)