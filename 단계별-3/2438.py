# 별 찍기 - 1

# N = int(input())
#
# for i in range(1, N+1):
#     for j in range(0, i):
#         print('*', end='')
#     print('')

N = int(input())

for i in range(1, N+1):
    print('*' * i)