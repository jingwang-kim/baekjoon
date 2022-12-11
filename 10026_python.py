import sys
from collections import deque

n = int(sys.stdin.readline())
graph = []
for _ in range(n):
    str = list(sys.stdin.readline().rstrip())
    graph.append(str)

graph2 = []
for i in range(n):
    tmp2 = []
    for j in graph[i]:
        tmp = j.replace('R','G')
        tmp2.append(tmp)
    graph2.append(tmp2)

dx = [0,0,1,-1]
dy = [1,-1,0,0]

def bfs1(a,b,color):
    q = deque([])
    q.append([a,b])
    graph[a][b] = 0
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] == color:
                q.append([nx,ny])
                graph[nx][ny] = 0

def bfs2(a,b,color):
    q = deque([])
    q.append([a,b])
    graph2[a][b] = 0
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n and graph2[nx][ny] == color:
                q.append([nx,ny])
                graph2[nx][ny] = 0

result1 = 0 #일반 사람
result2 = 0 #적록 색약

for i in range(n):
    for j in range(n):

        if graph[i][j] != 0:
            bfs1(i,j,graph[i][j])
            result1 += 1

        if graph2[i][j] != 0:
            bfs2(i,j,graph2[i][j])
            result2 += 1

print(result1, result2)