def find_largest(nums):
    largest=nums[0]
    for num in nums:
        if num>largest:
            largest=num
    return largest
print(find_largest([3, 7, 2, 9, 4])) # should print 9