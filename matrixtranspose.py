matrix = []
temp=0
row = int(input())
column = int(input())
for i in range(row):
    matrix.append(list(map(int,input().split())))
for i in range(row):
    for j in range(i+1,column):
        temp = matrix[i][j]
        matrix[i][j] = matrix[j][i]
        matrix[j][i] = temp
print(matrix)
                  
