import sys

n = int(sys.stdin.readline())
result = 0

for i in range(1,n+1):
    tmp = list(map(int,str(i)))
    result = i + sum(tmp)
    if result == n:
        print(i)
        break
    elif i == n:
        print(0)
