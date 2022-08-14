import sys

x = int(sys.stdin.readline())
n = int(sys.stdin.readline())
result = 0

for i in range(n):
    a,b = map(int,sys.stdin.readline().split())
    result += (a*b)

if result == x:
    print('Yes')
else:
    print('No')