import sys
sys.setrecursionlimit(10**9)

n,m = map(int,sys.stdin.readline().split())
visited = [0] * (n+1)

graph = [[] for _ in range(n+1)]
for _ in range(m):
    v,u = map(int,sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

for i in range(1,len(graph)):
    graph[i].sort()

def dfs(start):
    visited[start] = 1
    for i in graph[start]:
        if visited[i] == 0:
            dfs(i)

result = 0
for i in range(1,n+1):
    if visited[i] == 0:
        dfs(i)
        result += 1
print(result)