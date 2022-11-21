import sys
from collections import deque

n,k = map(int,sys.stdin.readline().split())
graph = [0 for _ in range(100001)]

def bfs():
    q=deque([])
    q.append(n)
    graph[n] = 1

    while q:
        x = q.popleft()
        if x == k:
            print(graph[k] - 1)
            break
        location = [x-1,x+1,x*2] #빼기, 더하기, 곱하기
        for i in range(3):
            nx = location[i]
            if 0 <= nx <= 100000 and graph[nx] == 0:
                graph[nx] = graph[x] + 1
                q.append(nx)

bfs()