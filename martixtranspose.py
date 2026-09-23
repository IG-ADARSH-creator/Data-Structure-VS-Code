rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

print("Enter matrix:")
A = []

for i in range(rows):
    row = list(map(int, input().split()))
    A.append(row)

transpose = []

for j in range(cols):
    row = []
    for i in range(rows):
        row.append(A[i][j])
    transpose.append(row)

print("Transpose of matrix:")

for row in transpose:
    print(*row)