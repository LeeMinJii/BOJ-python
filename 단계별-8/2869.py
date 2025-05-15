# 달팽이는 올라가고 싶다.
import math
a, b, v = map(int, input().split())

meter = 0
days = 0

if a >= v:
    print(1)
else:
    meter = a - b
    ramaining_meter = v - a
    days = math.ceil(ramaining_meter/meter)
    print(days+1) # 첫날 올라가는 1일 더하기

# while meter < v:
#     meter += a
#     if meter < v: # 정상이 아닐 때만 미끄러지기
#         meter -= b
#     days += 1