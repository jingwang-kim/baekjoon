import sys

n = int(sys.stdin.readline())
graph = []
for _ in range(n):
    graph.append(list(map(int,sys.stdin.readline().split())))

result = []
def solve(x,y,n):
    check = graph[x][y]
    for i in range(x,x+n):
        for j in range(y,y+n):
            if check != graph[i][j]:
                solve(x,y,n//3)
                solve(x,y+n//3,n//3)
                solve(x,y+n//3+n//3,n//3)
                solve(x+n//3,y,n//3)
                solve(x+n//3+n//3,y,n//3)
                solve(x+n//3,y+n//3,n//3)
                solve(x+n//3,y+n//3+n//3,n//3)
                solve(x+n//3+n//3,y+n//3,n//3)
                solve(x+n//3+n//3,y+n//3+n//3,n//3)
                return
    
    if check == 1:
        result.append(1)
    elif check == 0:
        result.append(0)
    else:
        result.append(-1)

solve(0,0,n)
print(result.count(-1))
print(result.count(0))
print(result.count(1))