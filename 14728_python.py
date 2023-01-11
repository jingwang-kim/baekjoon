import sys

n,t = map(int,sys.stdin.readline().split()) #단원 개수,공부할 수 있는 총 시간 
study = [[0,0]]
for _ in range(n):
    study.append(list(map(int,sys.stdin.readline().split()))) #예상 공부 시간, 그 단원 문제의 배점

dp = [[0 for _ in range(t+1)] for _ in range(n+1)]

for i in range(1,n+1):
    for j in range(1,t+1):
        time = study[i][0]
        score = study[i][1]

        if j >= time:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-time] + score)
        else:
            dp[i][j] = dp[i-1][j]

print(dp[n][t])