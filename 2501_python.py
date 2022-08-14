import sys

n,k = map(int,sys.stdin.readline().split())
common = []
result = 0

for i in range(1,n+1):
    if n % i == 0:
        common.append(i)

if len(common) < k:
    print(0)
else:
    print(common[k-1])