import sys

a,b,c = map(int,sys.stdin.readline().split())
result = 0

if b >= c:
    print(-1)

else:
    tmp = c - b
    result = a // tmp + 1
    print(result)