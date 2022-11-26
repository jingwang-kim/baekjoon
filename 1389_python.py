import sys
from collections import deque

#n = 유저의 수, m = 친구의 수
n,m = map(int,sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a,b = map(int,sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)


def bfs(start):
    visited = [0] * (n+1)
    q = deque([])
    q.append(start)


    while q:
        r = q.popleft()
        for i in graph[r]:
            if visited[i] == 0 and i != start:
                visited[i] = visited[r] + 1
                q.append(i)
    print(visited,sum(visited))
    return sum(visited)

# 6 8 5 5 8
check = sys.maxsize
result = 0
for i in range(1,n+1):
    flag = bfs(i)
    if check > flag:
        check = flag
        result = i

print(result)