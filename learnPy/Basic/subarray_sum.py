def subarraySum(nums, subtotal=0):
    # 查找子数组之和等于 subtotal 的子数组，返回第一次出现的子数组首尾下标
    length = len(nums)
    if length<1:
        return False
    for i in range(length):
        for j in range(i+1,length,1):
            sumNums = 0
            for k in range(i,j+1,1):
                sumNums += nums[k]
            if sumNums == subtotal:
                return [i,j]
            
nums = [4,1,2,-1,-2,2,3]
print(subarraySum(nums, 1)) 