import sys
from collections import deque

n = int(sys.stdin.readline())
k = int(sys.stdin.readline())
result = 0
dx = [0,1,0,-1]  #동서남북
dy = [1,0,-1,0]  #(0,1) = 동 ,(1,0) = 남 ,(0,-1) = 서 ,(-1,0) = 북

#보드 채우기
board = [[0 for _ in range(n)]for _ in range(n)]
for i in range(k):
    row,col = map(int,sys.stdin.readline().split())
    board[row-1][col-1] = 2

#뱀의 회전
l = int(sys.stdin.readline())
move=dict()
for j in range(l):
    x,c = sys.stdin.readline().split()
    move[int(x)] = c

snake = deque()
snake.append((0,0))
direction = 0 #뱀의 위치 결정

def turn(c):
    global direction
    if c == "L":
        direction = (direction-1)%4
    else:
        direction = (direction+1)%4

x,y = 0,0 #뱀의 머리 위치
while True:
    result += 1
    x += dx[direction]
    y += dy[direction]

    if x<0 or x>=n or y<0 or y>=n:
        break

    #사과 있으면 머리만 이동, 그렇지 않으면 둘 다 이동
    if board[x][y] == 2:
        board[x][y] = 1
        snake.append((x,y))
        if result in move:
            turn(move[result])

    elif board[x][y] == 0:
        board[x][y] = 1
        snake.append((x,y))
        tx,ty=snake.popleft()
        board[tx][ty] = 0
        if result in move:
            turn(move[result])

    else:
        break
print(result)