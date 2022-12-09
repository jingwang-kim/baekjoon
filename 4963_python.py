import sys
from collections import deque

def bfs(x,y):
    dx = [0,0,1,-1,-1,-1,1,1]
    dy = [1,-1,0,0,-1,1,-1,1]
    q = deque()
    graph[x][y] = 0
    q.append([x,y])
    while q:
        a,b = q.popleft()
        for i in range(8):
            nx = a + dx[i]
            ny = b + dy[i]

            if 0 <= nx < h and 0 <= ny < w and graph[nx][ny] == 1:
                graph[nx][ny] = 0
                q.append([nx,ny])

while True:
    w,h = map(int,sys.stdin.readline().split())
    if w == 0 and h == 0:
        break
    
    graph = []
    for _ in range(h):
        graph.append(list(map(int,sys.stdin.readline().split())))

    cnt = 0
    for i in range(h):
        for j in range(w):
            if graph[i][j] == 1:
                bfs(i,j)
                cnt += 1
    print(cnt)
