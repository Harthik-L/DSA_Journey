def binary_search_recursive(nums,target,left,right):
    if left>right:
        return -1
    mid=(left+right)//2
    if nums[mid]==target:
        return mid
    elif nums[mid]<target:
        return binary_search_recursive(nums,target,mid+1,right)
    else:
        return binary_search_recursive(nums,target,left,mid-1)
print(binary_search_recursive([1,3,5,7,9,11],7,0,5))  #3

