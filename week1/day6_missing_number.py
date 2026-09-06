def missing_number(nums,n):
    expected_sum=n*(n+1)//2
    actual_sum=sum(nums)
    return expected_sum-actual_sum
print(missing_number([1,2,4,5],5)) #3
