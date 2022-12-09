import sys

t = int(sys.stdin.readline())
graph = [[0 for _ in range(100)] for _ in range(100)]

for _ in range(t):
    n,m = map(int,sys.stdin.readline().split())
    
    for i in range(n,n+10):
        for j in range(m,m+10):
            graph[i][j] = 1

result = 0
for k in range(100):
    result += graph[k].count(1)
print(result)