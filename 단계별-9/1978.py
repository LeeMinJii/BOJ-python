# 소수 찾기
n = int(input())
nums = list(map(int, input().split()))

# 소수의 개수 출력
prime_nums = 0
for i in range(n):
    tmp = 0
    for j in range(1, nums[i]+1):
        if nums[i] % j == 0:
           tmp += 1
    if tmp == 2:
        prime_nums += 1

print(prime_nums)