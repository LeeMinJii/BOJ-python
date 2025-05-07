# 다이얼
dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']

s = input()
time = 0

for i in s: # s의 문자 하나씩 가져오기
    for j in dial: # 'ABC', 'DEF' ...하나씩 가져오기
        if i in j: # j에 i가 있으면 인덱스+3 반환
            num = dial.index(j) + 3
            time += num

print(time)