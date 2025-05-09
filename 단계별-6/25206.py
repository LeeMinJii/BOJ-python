# 너의 평점은
# rating = {'A+':4.5, 'A0':4.0, 'B+':3.5, 'B0':3.0, 'C+':2.5, 'C0':2.0, 'D+':1.5, 'D0':1.0, 'F':0.0}
# transcript = []
#
# # P는 계산에서 제외이므로 그 외 저장하기
# for _ in range(20):
#     s = list(input().split())
#     if s[2] == 'P':
#         pass
#     else:
#         transcript.append(s)
#
# grades = 0 # 학점 합
# sum = 0 # 학점*등급 합
#
# for i in range(len(transcript)):
#     sum += float(transcript[i][1]) * float(rating[transcript[i][2]])
#     grades += float(transcript[i][1])
#
# print(f'{sum/grades:.6f}')

rating = {'A+':4.5, 'A0':4.0, 'B+':3.5, 'B0':3.0, 'C+':2.5, 'C0':2.0, 'D+':1.5, 'D0':1.0, 'F':0.0}
grades = 0 # 학점 합
sum = 0 # 학점*등급 합

# P는 계산에서 제외이므로 그 외 저장하기
for _ in range(20):
    a, b, c = list(input().split())
    if c == 'P':
        continue
    else:
        sum += float(b) * float(rating[c])
        grades += float(b)

print(f'{sum/grades:.6f}')






