import sys

graph = []
for _ in range(9):
    graph.append(list(map(int,sys.stdin.readline().rstrip().split())))

maxi = 0
row = 0
col = 0
for i in range(9):
    for j in range(9):
        if graph[i][j] > maxi:
            maxi = graph[i][j]
            row = i
            col = j
print(maxi)
print(row, col)