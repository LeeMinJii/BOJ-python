# 문자열 반복
# t = int(input())
#
# for _ in range(t):
#     r, s = input().split()
#     r = int(r)
#     s = list(s)
#     for i in range(len(s)):
#         for x in range(r):
#             print(s[i], end='')
#     print()

t = int(input())

for _ in range(t):
    r, s = input().split() # 둘 다 문자열로 들어감
    res = ''
    for i in range(len(s)):
        res += s[i]*int(r)
    print(res)