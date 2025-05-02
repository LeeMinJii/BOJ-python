# 오븐 시계

a, b = map(int, input().split())
c = int(input())

a += c//60
b += c%60

if b>=60:
    a += 1
    b -= 60
    # 24부터 다시 0,1,..이 돼야하므로 24로 나눈 나머지
    print(a%24,b)
else:
    print(a%24, b)