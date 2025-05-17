# 분해합
n = int(input())

m = [] # 생성자

for i in range(1, n):
    tmp = i + sum((map(int, str(i))))
    if tmp == n:
        m.append(i)

if len(m) == 0:
    print(0)
else:
    print(min(m))