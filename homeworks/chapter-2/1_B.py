def summation(start, end):
    sum = 0
    steps = end-start+1
    for i in range(steps):
        sum+=start
        start+=1
    return sum

start,end = map(int,input().split(" "))
if start<=end:
    print(summation(start,end))
else:
    item = end
    end = start
    start = item
    print(summation(start,end))


