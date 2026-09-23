rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

print("Enter first matrix:")
A = []

for i in range(rows):
    row = list(map(int, input().split()))
    A.append(row)

print("Enter second matrix:")
B = []

for i in range(rows):
    row = list(map(int, input().split()))
    B.append(row)

C = []

for i in range(rows):
    row = []
    for j in range(cols):
        row.append(A[i][j] + B[i][j])
    C.append(row)

print("Matrix Addition:")

for row in C:
    print(*row)