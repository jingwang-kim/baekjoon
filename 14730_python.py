import sys

result = 0
n = int(sys.stdin.readline())

for _ in range(n):
    c,k = map(int,sys.stdin.readline().split())
    result += (c*k)

print(result)