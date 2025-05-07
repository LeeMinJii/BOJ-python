# 문자열
t = int(input())

for _ in range(t):
    s = str(input())
    print(s[0], s[-1], sep='')

# s[len(s)-1]가 아니라 맨 끝은 s[-1]이용!!