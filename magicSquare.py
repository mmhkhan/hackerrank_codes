my_matrix=[]
for _ in range(3):
    my_matrix.append(list(map(int, input().rstrip().split())))
sum_list = []
sum_list.extend([sum (lines) for lines in my_matrix])
for col in range(3):
    sum_list.append(sum(row[col] for row in my_matrix))
result1 = 0
for i in range(3):
    result1 +=my_matrix[i][i]
sum_list.append(result1)
result2 = 0
for i in range(2, -1, -1):
    result2 += my_matrix[i][i]
sum_list.append(result2)
print(sum_list)

