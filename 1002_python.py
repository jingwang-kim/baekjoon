import math
import sys

t = int(sys.stdin.readline())
for _ in range(t):
    #x1,y1 = a의 좌표, x2,y2 = b의 좌표, a가 계산한 c와의 거리 = r1, b가 계산한 c와의 거리 = r2
    #c가 있을 수 있는 좌표의 수 출력
    x1,y1,r1,x2,y2,r2 = map(int,sys.stdin.readline().split())
    dis = math.sqrt((x1-x2)**2 + (y1-y2) ** 2)
    
    if dis == 0:
        if r1 == r2:
            print(-1)
        else:
            print(0)
    
    else:
        if r1+r2 == dis or abs(r1-r2) == dis:
            print(1)
        elif r1+r2 < dis or abs(r1-r2) > dis:
            print(0)
        else:
            print(2)