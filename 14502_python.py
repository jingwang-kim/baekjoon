import sys
from collections import deque
import copy

n,m = map(int,sys.stdin.readline().split())
graph = []
for _ in range(n):
    graph.append(list(map(int,sys.stdin.readline().split())))

dx = [0,0,1,-1]
dy = [1,-1,0,0]

max_result = 0

def bfs():
    global max_result
    result = 0
    copy_graph = copy.deepcopy(graph)
    
    queue = deque([])
    for i in range(n):
        for j in range(m):
            if copy_graph[i][j] == 2:
                queue.append([i,j])

    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if (0<=nx<n and 0<=ny<m) and copy_graph[nx][ny] == 0:
                copy_graph[nx][ny] = 2
                queue.append([nx,ny])
    for i in range(n):
        result += copy_graph[i].count(0)
    
    max_result = max(max_result, result)
    


def wall(cnt):
    if cnt == 3:
        bfs()
        return
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                graph[i][j] = 1
                wall(cnt + 1)
                graph[i][j] = 0

wall(0)
print(max_result)