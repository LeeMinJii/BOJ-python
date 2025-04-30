# 공 넣기

N, M = map(int, input().split())

# 바구니에 공을 넣기 전에 크기 N만큼 0으로 초기화해야한다
basket = [0] * N

for _ in range(M):
    i, j, k = map(int, input().split())
    for x in range(i, j+1):
        basket[x-1] = k

print(*basket)