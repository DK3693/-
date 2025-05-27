A = []
for _ in range(9):
    A.append(list(map(int, input().split())))
    
A_max = 0
row = 0
col = 0

for i in range(9):
    for j in range(9):
        if A[i][j] >= A_max:
            A_max = A[i][j]
            row = j + 1
            col = i + 1
print(A_max)
print(col, row)