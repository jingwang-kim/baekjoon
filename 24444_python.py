import sys
from collections import deque
sys.setrecursionlimit(10 ** 9)

n,m,r = map(int,sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]
visited = [0] * (n+1)
cnt = 1

for _ in range(m):
    v,u = map(int,sys.stdin.readline().split())
    graph[v].append(u)
    graph[u].append(v)

for i in range(1,len(graph)):
    graph[i].sort()

def bfs(start):
    global cnt
    #노드를 방문하면서 인접한 노드 중 방문하지 않았던 노드의 정보면 큐에 넣어
    #큐에 먼저 들어있던 노드부터 방문
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