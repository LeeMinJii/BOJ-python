# 진법 변환 2
nums = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
n, b = map(int, input().split())
res = ''
# 10진법 -> b진법
# 더 안 나눠질 때까지 b로 나누며 나머지를 저장한다.

while n: # n이 0이면 반복 중단
    res += str(nums[n%b])
    n //= b

print(res[::-1])
