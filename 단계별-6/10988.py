# 팰린드롬인지 확인하기
s = input()
reversed_s = s[::-1]

if s == reversed_s:
    print(1)
else:
    print(0)