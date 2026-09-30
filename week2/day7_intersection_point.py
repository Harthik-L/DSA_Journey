def intersection_point(list1,list2):
    for item in list1:
        if item in list2:
            return item
    return None
print(intersection_point([1,2,3,4],[3,4,5,6]))
print(intersection_point([1,2],[3,4]))