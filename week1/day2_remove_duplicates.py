def remove_duplicates(nums):
    unique=[]
    for num in nums:
        if num not in unique:
            unique.append(num)
    return unique
print(remove_duplicates([1,2,2,3,4,4,5])) #[1,2,3,4,5]