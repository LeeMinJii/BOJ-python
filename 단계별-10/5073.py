# 삼각형과 세 변
while True:
    lines = list(map(int, input().split()))

    if sum(lines) == 0:
        break
    if max(lines) < sum(lines) - max(lines): # 가장 긴 변의 길이가 나머지 두변 합보다 클 때
        if len(set(lines)) == 1: # 세 변의 길이가 모두 같은 경우
            print('Equilateral')
        elif len(set(lines)) == 3: # 세 변의 길이가 모두 다른 경우
            print('Scalene')
        else:
            print('Isosceles')
    else:
        print('Invalid')