# 영수증
X = int(input())
N = int(input())

sum = 0

for i in range(0, N):
    a, b = map(int, input().split())
    tmp = a*b
    sum += tmp

if sum == X:
    print('Yes')
else:
    print('No')
