import sys

n,m,b = map(int,sys.stdin.readline().split())
land = []
for _ in range(n):
    land.append(list(map(int,sys.stdin.readline().split())))

# 1. 블록 제거하여 인벤토리에 저장 - 1초
# 2. 인벤토리에서 블록 하나를 꺼내 i,j의 가장 위에 있는 블록 위에 놓음 - 2초
# 최소 시간과 땅의 높이 출력

result = sys.maxsize
idx = 0
for target in range(257):
    maxi = 0
    mini = 0

    for i in range(n):
        for j in range(m):

            #블록이 층수보다 클 경우
            if land[i][j] >= target:
                maxi += land[i][j] - target
            
            #블록이 층수보다 작을 경우
            else:
                mini += target - land[i][j]
            
    if maxi + b >= mini:
        if mini + (maxi * 2) <= result:
            result = mini + (maxi * 2)
            idx = target
print(result, idx)