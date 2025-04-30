# 알람 시계

# 1
h, m = map(int, input().split())

if m>=45:
    m -= 45
elif h == 0:
    h = 23
    m += 15 # 60-45 + m
else:
    h -= 1
    m += 15

print(h, m)

# 2