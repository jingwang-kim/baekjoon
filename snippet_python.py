import sys
from collections import deque

#분할 정복
n = int(sys.stdin.readline())
graph = [list(map(int,sys.stdin.readline().strip())) for _ in range(n)]

def solution(x,y,n):
    check = graph[x][y]
    for i in range(x,x+n):
        for j in range(y,y+n):
            if check != graph[i][j]:
                print('(', end='')
                solution(x,y,n//2)
                solution(x,y+n//2,n//2)
                solution(x+n//2,y,n//2)
                solution(x+n//2,y+n//2,n//2)
                print(')', end='')
                return
            
    if check == 0:
        print(0, end='')
    else:
        print(1, end='')

solution(0,0,n)

#