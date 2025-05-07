# 그대로 출력하기

# try-except 이용
# while True:
#     try:
#         data = input()
#         print(data)
#     except EOFError:
#         break

# sys.stdin.read() 이용
# import sys
# data = sys.stdin.read()
# print(data)

import sys
for line in sys.stdin:
    print(line, end='')