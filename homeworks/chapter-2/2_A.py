def ladder(previous, n):
    if n==0:
        return 1
    levels = 0
    for i in range(previous):
        if n-i>=0:
            levels+=ladder(i, n-i)
    return levels

n = int(input())
count = 0
count+=ladder(n+1, n)
print(count)
        

    
