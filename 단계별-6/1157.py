# 단어 공부

# lower()-소문자로 저장 / upper()-대문자로 저장
words = list(input().upper())

# 중복 제거한 리스트
unique_words = list(set(words))

cnt_list =[]

# unique_words에 있는 알파벳 하나씩 원래 문장(words)에서 개수 세기
for i in unique_words:
    cnt = words.count(i)
    cnt_list.append(cnt) # 각 알파벳 개수 append

if cnt_list.count(max(cnt_list)) > 1:
    print('?')
else:
    max_index = cnt_list.index(max(cnt_list))
    print(unique_words[max_index])