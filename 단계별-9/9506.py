# 약수들의 합
while True:
    n = int(input())
    if n == -1:
        break

    #약수 리스트에 담기
    factor = []
    for i in range(1, n+1):
        if n % i == 0:
            factor.append(i)

    if sum(factor[:-1]) == n:
        # join이용해서 리스트 사이를 +로 연결
        factor_str = ' + '.join((map(str, factor[:-1])))
        print(f'{n} = {factor_str}')
    else:
        print(f'{n} is NOT perfect.')