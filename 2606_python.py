import sys

computer = int(sys.stdin.readline())
net = int(sys.stdin.readline())
graph = [[] for _ in range(computer+1)]
visited = [False]*(computer+1) #True가 되면 감염된 것

for _ in range(net):
    v,u = map(int,sys.stdin.readline().split())
    graph[v].append(u)
    graph[u].append(v)

for i in range(1,len(graph)):
    graph[i].sort

def dfs(start):
    visited[start] = True
    for i in graph[start]:
        if visited[i] == False:
            visited[i] = True
            dfs(i)

dfs(1)
result = 0

for i in visited[2:]:
    if i:
        result += 1

print(result)
