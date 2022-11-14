import sys

n = int(sys.stdin.readline())
graph = []

for _ in range(n):
    graph.append(list(map(int,sys.stdin.readline().rstrip())))


# 북, 남, 동, 서
dx = [0,0,1,-1]
dy = [1,-1,0,0]

cnt = 0
result = []

def dfs(x,y):

    if x < 0 or x >= n or y < 0 or y>=n:
        return False

    if graph[x][y] == 1:
        global cnt
        graph[x][y] = 0
        cnt += 1

        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            dfs(nx,ny)
        return True
    return False

for i in range(n):
    for j in range(n):
        if dfs(i,j):
            result.append(cnt)
            cnt = 0

result.sort()
print(len(result))
for i in result:
    print(i)