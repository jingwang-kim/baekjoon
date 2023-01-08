import sys
from collections import deque

def bfs(start):
    q = deque([])
    q.append(start)
    visited[start] = True
    while q:
        x = q.popleft()
        for i in range(1,7):
            move = x + i
            if 0<move<=100 and not visited[move]:
                if move in lad.keys():
                    move = lad[move]
                
                if move in snake.keys():
                    move = snake[move]
                
                if not visited[move]:
                    q.append(move)
                    visited[move] = True
                    graph[move] = graph[x] + 1
            



n,m = map(int,sys.stdin.readline().split())
graph = [0 for _ in range(101)]
visited = [False] * 101

lad = dict()
for _ in range(n):
    a,b = map(int,sys.stdin.readline().split())
    lad[a] = b

snake = dict()
for _ in range(m):
    a,b = map(int,sys.stdin.readline().split())
    snake[a] = b

bfs(1)
print(graph[100])