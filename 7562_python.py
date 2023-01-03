import sys
from collections import deque

dx = [1,2,2,1,-1,-2,-2,-1]
dy = [2,1,-1,-2,-2,-1,1,2]
    
def bfs(sx,sy,ex,ey):
    q = deque([])
    q.append([sx,sy])
    graph[sx][sy] = 1
    while q:
        x,y = q.popleft()
        if x == ex and y == ey:
            print(graph[ex][ey] - 1)

        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<=nx<l and 0<=ny<l and graph[nx][ny] == 0:
                q.append([nx,ny])
                graph[nx][ny] = graph[x][y] + 1



t = int(sys.stdin.readline())
for _ in range(t):
    l = int(sys.stdin.readline()) #l *l 의 체스판 생성
    sx,sy = map(int,sys.stdin.readline().split())
    ex,ey = map(int,sys.stdin.readline().split())
    graph = [[0 for _ in range(l)] for _ in range(l)]
    bfs(sx,sy,ex,ey)