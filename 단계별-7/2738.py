# 행렬 덧셈
n, m = map(int, input().split())

A, B = [], []

for i in range(n):
    tmp = list(map(int, input().split()))
    A.append(tmp)

for i in range(n):
    tmp = list(map(int, input().split()))
    B.append(tmp)

for i in range(n): # n개의 행
    for j in range(m): # n행에 있는 m개의 요소 각각 더하기
        result = A[i][j] + B[i][j]
        print(result, end=' ')
    print()