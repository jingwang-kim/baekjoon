import sys
sys.setrecursionlimit(10 ** 9)

n,m,r = map(int,sys.stdin.readline().split())

visited = [0]*(n+1)
graph = [[] for _ in range(n+1)]
cnt = 1

for _ in range(m):
    v,u = map(int,sys.stdin.readline().split())
    graph[v].append(u)
    graph[u].append(v)

for i in range(1,len(graph)):
    graph[i].sort(reverse=True)


def dfs(start):
    global cnt
    visited[start] = cnt
    for i in graph[start]:
        if visited[i] == 0:
            cnt += 1
            dfs(i)


dfs(r)
for i in range(1,n+1):
    print(visited[i])