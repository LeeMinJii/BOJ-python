# 평균
n = int(input())
grades = list(map(int, input().split()))
m = max(grades)

new_grades = [x/m*100 for x in grades]

print(sum(new_grades)/len(new_grades))