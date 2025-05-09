# 최댓값

matrix = []
for _ in range(3):
    a = list(map(int, input().split()))
    matrix.append(a)

# 최댓값과 인덱스 출력
max_value = matrix[0][0]
max_index = [0, 0]

for i in range(3):
    for j in range(3):
        if max_value <= matrix[i][j]:
            max_value = matrix[i][j]
            max_index[0], max_index[1] = i+1, j+1

print(max_value)
print(*max_index)