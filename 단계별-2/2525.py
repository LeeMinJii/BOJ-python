# 오븐 시계

# 1
h, m = map(int, input().split())
ctime = int(input())

if ctime+m < 60:
    m = m+ctime
else: # ctime+m >= 60
    if h == 23:
        h = ((ctime + m)//60)-1
    else:
        h += (ctime+m)//60
    m = (ctime+m)%60

print(h, m)