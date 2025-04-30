# 별 찍기 - 2
# N = int(input())
#
# for i in range(1, N+1):
#     stars = '*' * i
#     print(stars.rjust(N))

###################

# N = int(input())
#
# for i in range(1, N+1):
#     print(f'{"*" * i:>{N}}')

##################

N = int(input())

for i in range(1, N+1):
    stars = '*' * i
    print(f'{stars:>{N}}')