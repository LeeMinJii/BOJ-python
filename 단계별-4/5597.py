# 과제 안 내신 분..?

# numbers = []
# for _ in range(28):
#     a = int(input())
#     numbers.append(a)
#
# st_num = []
# for i in range(1, 31):
#     if i not in numbers:
#         st_num.append(i)
#
# print(min(st_num), max(st_num))

student = [i for i in range(1, 31)]

for _ in range(28):
    a = int(input())
    student.remove(a)

print(min(student), max(student))