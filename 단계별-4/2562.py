# 최댓값
numbers = []
for i in range(9):
    a = int(input())
    numbers.append(a)

print(max(numbers), numbers.index(max(numbers)) + 1)