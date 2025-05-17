# 세 막대
lines = list(map(int, input().split()))

max_line = max(lines)
other_lines = sum(lines)-max_line

if max_line < other_lines: # 삼각형 조건 만족할때
    print(sum(lines))
else: # 제일 긴 변이 나머지 두 변의 합보다 짧아질때까지 -1
    while max_line >= other_lines:
        max_line -= 1
    print(max_line + other_liㄷnes)