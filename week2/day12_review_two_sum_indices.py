def two_sum_indices(nums,target):
    seen={}
    for i, num in enumerate(nums):
        complement=target-num
        if complement in seen:
            return (seen[complement],i)
        seen[num]=i
    return None
print(two_sum_indices([2,7,11,15],9))   #(0,1)