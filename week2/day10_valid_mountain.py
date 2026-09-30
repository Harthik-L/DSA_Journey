def valid_mountain(nums):
    n=len(nums)
    if n<3:
        return False
    i=0
    while i<n-1 and nums[i]<nums[i+1]:
        i+=1
    if i==0 or i==n-1:
        return False
    while i<n-1 and nums[i]>nums[i+1]:
        i+=1
    return i==n-1

print(valid_mountain([0,3,2,1]))  #True
print(valid_mountain([3,5,5]))   #False (flat top,not strictly increasing)