import sys

dx = [0,0,1,-1]
dy = [-1,1,0,0]
visited = set()

def dfs(x,y,cnt):
    global result
    result = max(result, cnt)
    visited.add(graph[x][y])

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0<=nx<r and 0<=ny<c and graph[nx][ny] not in visited:
            dfs(nx,ny,cnt+1)
    
    visited.remove(graph[x][y])




r,c = map(int,sys.stdin.readline().split())
graph = []
result = 0
for _ in range(r):
    graph.append(list(sys.stdin.readline().rstrip()))
dfs(0,0,1)
print(result)