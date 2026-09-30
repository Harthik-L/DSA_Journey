def matrix_sum(matrix):
    total=0
    for row in matrix:
        for num in row:
            total+=num
    return total

grid=[[1,2,3],[4,5,6],[7,8,9]]
print(matrix_sum(grid))    #45