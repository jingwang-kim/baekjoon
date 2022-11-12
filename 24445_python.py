import sys
from collections import deque
sys.setrecursionlimit(10**9)

n,m,r = map(int,sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]
visited = [0] * (n+1)

for _ in range(m):
    v,u = map(int,sys.stdin.readline().split())
    graph[v].append(u)
    graph[u].append(v)

cnt = 1

for i in range(1,len(graph)):
    graph[i].sort(reverse=True)

def bfs(start):
    global cnt
    queue = deque([start])
    visited[start] = 1

    while queue:
        start = queue.popleft()
        for i in graph[start]:
            if visited[i] == 0:
                cnt += 1
                visited[i] = cnt
                queue.append(i)
bfs(r)
for i in visited[1:]:
    print(i)