# 곱셈

# 1
# a = int(input())
# b = int(input())
#
# c = a*(b%10) # b에서 일의 자리만 남기기
# d = a*(b%100//10) # b에서 십의 자리만 남기기
# e = a*(b//100) # b에서 백의 자리만 남기기
# sum = (a*b)
#
# print(c)
# print(d)
# print(e)
# print(sum)

# 2
a = int(input())
b = list(input())

one = int(b[2])
ten = int(b[1])
hundred = int(b[0])

num3 = a*one
num4 = a*ten
num5 = a*hundred

print(num3)
print(num4)
print(num5)

print(num3+num4*10+num5*100)
