# 블랙잭
n, m = map(int,input().split())

cards = list(map(int, input().split()))

# 3개의 카드 고르기 = n(n-1)(n-2)
res = []
for i in range(n): # n개중에 숫자 하나 고르기
    for j in range(i+1, n): # 첫 반복문 때 고른 거 빼고 나머지 n-1개 중 하나
        for x in range(j+1, n): # 남은 n-2개 중 마지막 세번째 숫자 고르기
            tmp = cards[i] + cards[j] + cards[x]
            if tmp <= m:
                res.append(tmp)

print(max(res))