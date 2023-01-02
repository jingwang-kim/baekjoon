import sys

#백트래킹은 대부분 DFS로 구현 -> dfs를 쓰지 않는 경우는 트리의 깊이가 무한대가 될 때

n = int(sys.stdin.readline())
result = sys.maxsize
visited = [False] * (n+1)

s = []
for _ in range(n):
    s.append(list(map(int,sys.stdin.readline().split())))

def dfs(depth,index):
    global result
    if depth == (n//2):
        start, link = 0, 0
        for i in range(n):
            for j in range(i+1,n):
                if visited[i] and visited[j]:
                    start += (s[i][j] + s[j][i])
                elif not visited[i] and not visited[j]:
                    link += (s[i][j] + s[j][i])
        
        result = min(result, abs(start-link))
    for i in range(index,n):
        if not visited[i]:
            visited[i] = True
            dfs(depth+1,i+1)
            visited[i] = False

dfs(0,0)
print(result)