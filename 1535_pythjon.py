import sys

n = int(sys.stdin.readline())
health = [0] + list(map(int,sys.stdin.readline().split()))
happy = [0] + list(map(int,sys.stdin.readline().split()))

dp = [[0 for _ in range(101)] for _ in range(n+1)]

for i in range(1,n+1):
    for j in range(1,101):
        
        #max(i-1 개의 물건들을 갖고 구한 전 단계의 값, i 번째 물건만큼의 무게를 비웠을 때의 값 + i 번째 물건)
        if j >= health[i]:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-health[i]] + happy[i])

        else:
            dp[i][j] = dp[i-1][j]
print(dp[n][99])