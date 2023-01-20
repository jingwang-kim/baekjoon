import sys

#첫 색상이 나머지 색상과 같은지 확인 후 틀린 것이 있으면, 틀린 구역을 다시 네 구역으로 나누어 다시 색상이 같은 것을 확인

n = int(sys.stdin.readline())
graph = []
for _ in range(n):
    graph.append(list(map(int,sys.stdin.readline().split())))

result = []

def solution(x,y,n):
    color = graph[x][y]
    for i in range(x,x+n):
        for j in range(y,y+n):
            if color != graph[i][j]:
                solution(x,y,n//2) #2사분면
                solution(x,y+n//2,n//2) #1사분면
                solution(x+n//2,y,n//2) #3사분면
                solution(x+n//2,y+n//2,n//2) #4사분면
                return
    if color == 0:
        result.append(0)
    else:
        result.append(1)

#0,0부터 재귀를 돌며 색종이의 개수를 세기 시작
solution(0,0,n)
#하얀 색종이의 개수
print(result.count(0))
#파란 색종이의 개수
print(result.count(1))