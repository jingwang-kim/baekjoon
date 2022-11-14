import sys
from collections import deque

dx = [0,0,1,-1]
dy = [1,-1,0,0]


def bfs(graph,a,b):
    q = deque()      #queue 만듦
    q.append([a,b])  #queue에 현재좌표 넣음
    graph[a][b] = 0  #현재 좌표 방문 했으므로 0으로 바꿔줌
    cnt = 1

    while q:
        x,y = q.popleft()   #queue의 제일 첫번째 값(제일 우선순위인 값) pop
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            if nx<0 or nx>=n or ny < 0 or ny >=n:
                continue
            if graph[nx][ny] == 1:   #한 칸 이동한 값이 1이면
                graph[nx][ny] = 0    #방문했으므로 0으로 바꿈
                q.append([nx,ny])    #queue에 다음 방문 위치 저장
                cnt += 1
    return cnt


n = int(sys.stdin.readline())
graph = []
result = []

for _ in range(n):
    graph.append(list(map(int,sys.stdin.readline().rstrip())))

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:    #현재 그래프 좌표가 1이면 
            result.append(bfs(graph,i,j))  #bfs를 통해 주면 단지 구함

result.sort()
print(len(result))
for i in result:
    print(i)