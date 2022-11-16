import sys

n,m = map(int,sys.stdin.readline().split())
board = []
result = []
for _ in range(n):
    board.append(list(sys.stdin.readline().rstrip()))

for a in range(n-7):
    for b in range(m-7):
        index1 = 0  #W로 시작했을 때
        index2 = 0  #B로 시작했을 때

        for i in range(a,a+8):
            for j in range(b,b+8):
                # 행과 열의 합이 짝수면 시작점의 색과 같아야 함 
                if (i+j) % 2 == 0:
                    if board[i][j] != 'W':
                        index1 += 1
                    if board[i][j] != 'B':
                        index2 += 1

                #홀수면 시작점의 색과 달라야 함
                else:
                    if board[i][j] != 'B':
                        index1 += 1
                    if board[i][j] != 'W':
                        index2 += 1
        result.append(min(index1,index2))
print(min(result))