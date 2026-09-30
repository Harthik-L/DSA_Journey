def remove_element(nums,val):
    k=0
    for i in range(len(nums)):
        if nums[i]!=val:
            nums[k]=nums[i]
            k+=1
    return k
nums=[3,2,2,3,4]
new_length=remove_element(nums,3)
print(new_length)          #3
print(nums[:new_length])   #[2,2,4]