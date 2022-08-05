import sys

n = int(sys.stdin.readline())
peak = list(map(int,sys.stdin.readline().split()))
result = 0
cur = 0
flag = peak[0]

for i in peak:
    if flag > i:
        cur += 1
    else:
        result = max(cur, result)
        flag = i
        cur = 0
print(result)