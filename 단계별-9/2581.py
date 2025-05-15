# 소수
m = int(input())
n = int(input())

prime_nums = []
for i in range(m, n+1): # m이상 n이하
    tmp = 0
    # 약수 개수 검사
    for j in range(1, i+1):
        if i % j == 0:
            tmp += 1
    # 소수면 리스트에 넣기
    if tmp == 2:
        prime_nums.append(i)

if len(prime_nums) < 1:
    print(-1)
else:
    print(sum(prime_nums))
    print(min(prime_nums))