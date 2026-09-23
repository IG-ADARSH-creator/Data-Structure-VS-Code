r1 = int(input("Enter rows of first matrix: "))
c1 = int(input("Enter columns of first matrix: "))

print("Enter first matrix:")
A = []

for i in range(r1):
    row = list(map(int, input().split()))
    A.append(row)

r2 = int(input("Enter rows of second matrix: "))
c2 = int(input("Enter columns of second matrix: "))

if c1 != r2:
    print("Matrix multiplication is not possible.")
else:
    print("Enter second matrix:")
    B = []

    for i in range(r2):
        row = list(map(int, input().split()))
        B.append(row)

    C = [[0 for j in range(c2)] for i in range(r1)]

    for i in range(r1):
        for j in range(c2):
            for k in range(c1):
                C[i][j] += A[i][k] * B[k][j]

    print("Matrix Multiplication:")

    for row in C:
        print(*row)