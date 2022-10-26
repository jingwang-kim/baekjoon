import sys

n = int(sys.stdin.readline())
arr = list(map(int,sys.stdin.readline().split()))
v = int(sys.stdin.readline())
result = 0

for i in arr:
    if i == v:
        result += 1

print(result)