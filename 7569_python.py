import sys
from collections import deque

#n = 행, m = 열, h = 높이(쌓아올려지는 상자의 수)
m,n,h = map(int,sys.stdin.readline().split())
graph = []
q = deque([])

for i in range(h):
    tmp = []
    for j in range(n):
        tmp.append(list(map(int,sys.stdin.readline().split())))
        for k in range(m):
            if tmp[j][k] == 1:
                q.append([i,j,k])
    graph.append(tmp)

dx = [0,0,1,-1,0,0]
dy = [1,-1,0,0,0,0]
dz = [0,0,0,0,1,-1]

while q:
    x,y,z = q.popleft()
    for i in range(6):
        nx = x + dx[i]
        ny = y + dy[i]
        nz = z + dz[i]

        if 0 <= nx < h and 0 <= ny < n and 0 <= nz < m and graph[nx][ny][nz] == 0:
            graph[nx][ny][nz] = graph[x][y][z] + 1
            q.append([nx,ny,nz])

result = 0
for i in graph:
    for j in i:
        for k in j:
            if k == 0:
                print(-1)
                exit(0)
        result = max(result, max(j))
print(result-1)