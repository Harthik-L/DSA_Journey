def max_sum_subarray(nums,k):
    window_sum=sum(nums[:k])
    max_sum=window_sum
    for i in range(k,len(nums)):
        window_sum+=nums[i]-nums[i-k]
        if window_sum>max_sum:
            max_sum=window_sum
    return max_sum
print(max_sum_subarray([2,1,5,1,3,2],3))     #9  (5+1+3)