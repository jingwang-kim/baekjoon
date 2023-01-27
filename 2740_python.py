import sys

n,m = map(int,sys.stdin.readline().split())
a = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]

m,k = map(int,sys.stdin.readline().split())
b = [list(map(int,sys.stdin.readline().split())) for _ in range(m)]

result = [[0 for _ in range(k)] for _ in range(n)]
for i in range(n):
    for j in range(k):
        for c in range(m):
            result[i][j] += a[i][c] * b[c][j]

for i in result:
    for j in i:
        print(j,end=' ')
    print()