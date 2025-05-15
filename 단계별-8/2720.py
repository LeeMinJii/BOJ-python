# 세탁소 사장 동혁
# t = int(input())
#
# for _ in range(t):
#     cent = int(input())
#     Q = cent//25
#     D = (cent%25) //10
#     N = ((cent%25)%10) //5
#     P = ((cent%25)%10)%5
#     print(Q, D, N, P)

t = int(input())

for _ in range(t):
    cent = int(input())
    for i in [25, 10, 5, 1]:
        print(cent//i, end=' ')
        cent %= i