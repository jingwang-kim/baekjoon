import sys
sys.setrecursionlimit(10**9)

m,n = map(int,sys.stdin.readline().split())
graph = []
for _ in range(m):
    graph.append(list(map(int,sys.stdin.readline().split())))
dp = [[-1 for _ in range(n)] for _ in range(m)]

result = 0
dx = [0,0,1,-1]
dy = [1,-1,0,0]

def dfs(x,y):
    if x == m-1 and y == n-1:
        return 1
    if dp[x][y] != -1:
        return dp[x][y]

    cnt = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0<=nx<m and 0<=ny<n and graph[x][y] > graph[nx][ny]:
            cnt += dfs(nx,ny)
    dp[x][y] = cnt
    return dp[x][y]

print(dfs(0,0))