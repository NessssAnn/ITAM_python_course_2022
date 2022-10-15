def summation(nums):
    sum = 0
    for i in range(len(nums)):
        if nums[i]<0:
            nums[i]=abs(nums[i])*2
    maxnum = max(nums)
    for i in range(len(nums)):
        nums[i]=nums[i]/maxnum
        sum+=nums[i]
    return(sum)
list = list(map(int, input().split(" ")))
print(summation(list))
#не поняла в каком виде подаются числа на вход, изначально делала функцию с *args