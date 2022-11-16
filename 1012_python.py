import sys
sys.setrecursionlimit(10**9)

dx = [0,0,-1,1]
dy = [1,-1,0,0]

def dfs(graph,x,y):
    if x < 0 or y < 0 or x >= len(graph) or y >= len(graph[0]):
        return False

    if graph[x][y] == 1:
        graph[x][y] = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            dfs(graph,nx,ny)
        return True
    return False

t = int(sys.stdin.readline())
for _ in range(t):
    n,m,k = map(int,sys.stdin.readline().split())
    graph = [[0 for _ in range(m)] for _ in range(n)]

    for _ in range(k):
        a,b = map(int,sys.stdin.readline().split())
        graph[a][b] = 1
    
    result = 0
    for i in range(n):
        for j in range(m):
            if dfs(graph,i,j):
                result += 1
    print(result)