import sys
from collections import deque

n = int(sys.stdin.readline())
graph = []
for _ in range(n):
    graph.append(list(map(int,sys.stdin.readline().split())))
    flag = max(graph)
flag = max(flag)

result = 0
dx = [0,0,1,-1]
dy = [1,-1,0,0]


def bfs(a,b,depth,visited):
    q = deque([])
    q.append([a,b])
    visited[a][b] = 1

    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<n:
                if visited[nx][ny] == 0 and graph[nx][ny] > depth:
                    q.append([nx,ny])
                    visited[nx][ny] = 1


for k in range(flag):
    visited = [[0 for _ in range(n)] for _ in range(n)]
    tmp = 0

    for i in range(n):
        for j in range(n):
            if visited[i][j] == 0 and graph[i][j] > k:
                bfs(i,j,k, visited)
                tmp += 1

    if result < tmp:
        result = tmp
print(result)