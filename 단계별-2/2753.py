# 윤년

lyear = int(input())

# (4의 배수이면서 100의 배수가 아닌 경우) 또는 (4의배수)
if (lyear%4 == 0 and lyear%100 != 0) or (lyear%400 == 0):
    print('1')
else:
    print('0')