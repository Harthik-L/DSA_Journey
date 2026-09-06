def get_evens(nums):
    evens=[]
    for num in nums:
        if num%2==0:
            evens.append(num)
    return evens
print(get_evens([1,2,3,4,5,6])) #[2,4,6]