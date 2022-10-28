import sys

tri = [[1] * i for i in range(1, 31)]
n,k=map(int,sys.stdin.readline().split())

for i in range(2,30):
    for j in range(1, i):
        tri[i][j] = tri[i-1][j-1] + tri[i-1][j]
print(tri[n-1][k-1])