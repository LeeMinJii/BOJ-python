# 알파벳 찾기
# s = list(input())
# alphabet = 'abcdefghijklmnopqrstuvwxyz'
#
# for i in alphabet:
#     if i in s:
#         print(s.index(i), end=' ')
#     else:
#         print(-1, end=' ')

s = str(input())
alphabet = 'abcdefghijklmnopqrstuvwxyz'

for i in alphabet:
    print(s.find(i), end=' ')