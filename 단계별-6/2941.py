# 크로아티아 알파벳
croatia_alphabet = ['dz=', 'lj', 'nj', 'c=', 'c-', 'd-', 's=', 'z=']
word = input()

# 크로아티아 알파벳 개수 세기
for i in croatia_alphabet:
    word = word.replace(i, '*')

# 최종 개수 출력
print(len(word))