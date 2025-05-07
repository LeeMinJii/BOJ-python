# 상수
a, b = input().split()

# 슬라이싱 이용
reversed_a = a[::-1]
reversed_b = b[::-1]

print(max(reversed_a, reversed_b))