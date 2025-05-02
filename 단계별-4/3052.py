# 나머지

remainder = []

for _ in range(10):
    a = int(input())
    remainder.append(a%42)

# set()으로 중복 숫자 제거
remainder = list(set(remainder))

# len()으로 개수 세서 출력
print(len(remainder))