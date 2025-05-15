# 배수와 약수
while True:
    a, b = map(int, input().split())
    if a==0 and b==0:
        break
    else:
        if b % a == 0: # a가 b의 약수일 때
            print('factor')
        elif a % b == 0: # a가 b의 배수일 때
            print('multiple')
        else:
            print('neither')