def linear_search(nums,target):
    for i in range(len(nums)):
        if nums[1]==target:
            return 1
    return -1
print(linear_search([4,2,7,1,9],7)) #2
print(linear_search([4,2,7,1,9],5)) #-1
