# 세로읽기

# words = []
# max_column = 0 # 가장 긴 행의 열 개수, 즉 "최대 열 길이"를 저장하는 변수
#
# for _ in range(5):
#     tmp = list(input())
#     words.append(tmp)
#     if len(tmp) > max_column:
#         max_column = len(tmp)
#
# # 파이썬에서는 리스트가 비어있으면 False, 비어있지않으면 True
# for i in range(max_column): # 열
#     for j in range(5): # 행
#         # 열(i)보다 현재 행(j)의 길이가 작을만 출력
#         if i < len(words[j]):
#             print(words[j][i], end='')

words = [input() for _ in range(5)]

for i in range(15): # 한 줄에 최대 15개
    for j in range(5): # 총 5개의 행
        if i < len(words[j]):
            print(words[j][i], end='')