# 시험 성적

# 1
# res = int(input())
#
# if 90<=res<=100:
#     print('A')
# elif 80<=res<90:
#     print('B')
# elif 70<=res<80:
#     print('C')
# elif 60<=res<70:
#     print('D')
# else: print('F')

# 2
# res = int(input())
#
# if 90<=res<=100:
#     print('A')
# elif res>=80:
#     print('B')
# elif res>=70:
#     print('C')
# elif res>=60:
#     print('D')
# else: print('F')


# 3
res = int(input())

# 10으로 나눈 몫을 0 1 2 3 4 5 6 7 8 9 10 라고 하면
# 각각 여기에 점수 F F F F F F D C B A A 를 리스트에 넣어둔다.
grade = 'FFFFFFDCBAA'
print(grade[res//10])