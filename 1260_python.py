import sys
from collections import deque
sys.setrecursionlimit(10**9)

n,m,r = map(int,sys.stdin.readline().split())
visited_dfs = [0] * (n+1)
visited_bfs = [0] * (n+1)
graph = [[] for _ in range(n+1)]

for _ in range(m):
    v,u = map(int,sys.stdin.readline().split())
    graph[v].append(u)
    graph[u].append(v)

for i in range(1,len(graph)):
    graph[i].sort()

def dfs(start):
    visited_dfs[start] = 1
    print(start,end=' ')
    for i in graph[start]:
        if visited_dfs[i] == 0:
            dfs(i)

def bfs(start):
    visited_bfs[start] = 1
    q = deque([start])

    while q:
        start = q.popleft()
        print(start,end=' ')
        for i in graph[start]:
            if visited_bfs[i] == 0:
                visited_bfs[i] = 1
                q.append(i)

dfs(r)
print()
bfs(r)