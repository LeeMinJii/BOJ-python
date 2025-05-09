# 별 찍기 - 7
n = int(input())

# 별이 홀수 개로 늘어남 - (2*i-1)
# 짝수면 2*i

for i in range(1, n+1):
    print(' ' * (n-i) + '*' * (2*i-1))

for i in range(n-1, 0, -1): # 반복문 역순으로 돌리기
    print(' ' * (n-i) + '*' * (2*i-1))