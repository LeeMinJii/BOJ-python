# 진법 변환
# nums = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

# n, b = input().split()
# n = n[::-1] # 역순으로 만들기
# b = int(b)
#
# # b진법 -> 10진법
# # res = b의0제곱 * n[0] + b1 * n[1] ...
# # res += bi * n[i]
#
# res = 0
# for i in range(len(n)):
#     res += (int(b) ** i) * (nums.index(n[i]))
#
# print(res)

n, b = input().split()
print(int(n, int(b)))