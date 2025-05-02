# 주사위 세개
# dice = list(map(int, input().split()))
#
# set_dice = list(set(dice))
#
# if len(set_dice) == 1:
#     sum = 10000+(set_dice[0])*1000
#     print(sum)
#
# elif len(set_dice) == 2:
#
# else:
#     print(max(set_dice)*100)

a, b, c = map(int, input().split())

if a == b == c:
    print(10000+a*1000)
elif a == b or a == c:
    print(1000+a*100)
elif b == c:
    print(1000+b*100)
else:
    print(max(a, b, c)*100)