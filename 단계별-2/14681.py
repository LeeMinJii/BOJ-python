# 사분면 고르기

# 1
# x = int(input())
# y = int(input())
#
# if x>0:
#     if y>0:
#         print('1')
#     else:
#         print('4')
# else:
#     if y>0:
#         print('2')
#     else:
#         print('3')

# 2
x = int(input())
y = int(input())

if x>0 and y>0:
    print('1')
elif x>0 and y<0:
    print('4')
elif x<0 and y>0:
    print('2')
elif x<0 and y<0:
    print('3')
