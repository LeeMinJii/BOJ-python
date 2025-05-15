# 소인수분해
n = int(input())

if n == 1:
    exit()

i = 2
while n > 1:
    while n % i == 0:
        n //= i # 정수 나눗셈 //
        print(i)
    i += 1