# 색종이
n = int(input())

# 도화지 초기화 (100*100)
papers = [[0]*100 for _ in range(100)]

# 색종이만큼 도화지 1로 색칠하기
for i in range(n):
    x, y = map(int, input().split())
    for i in range(x, x+10):
        for j in range(y, y+10):
            papers[i][j] = 1

# 리스트 요소 다 더해서 1의 개수 세기
cnt = 0
for i in papers:
    cnt += sum(i)
print(cnt)