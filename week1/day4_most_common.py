def most_common(nums):
    freq={}
    for num in nums:
        freq[num]=freq.get(num,0)+1
    best_item=None
    highest_count=0
    for item,count in freq.items():
        if count>highest_count:
            highest_count=count
            best_item=item
    return best_item,highest_count
print(most_common([1,2,2,3,3,3,4]))