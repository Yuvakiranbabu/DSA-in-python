matrix=[[1,2,3],[4,5,6],[7,8,9]]

diagonal_sum=0
for i in range(len(matrix)):
    for j in range(len(matrix)):
        if i==j:
            diagonal_sum+=matrix[i][j]
        else:
            continue

print(diagonal_sum)