def pairs_with_diff_k(nums,k):
    count=0
    for i in range(len(nums)):
        for j in range(len(nums)):
            if i!=j and nums[i]-nums[j]==k:
                count+=1
    return count
print(pairs_with_diff_k([1,5,3,4,2],2))   #3