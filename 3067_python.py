import sys

t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline()) #동전의 가짓수
    coins = list(map(int,sys.stdin.readline().split()))
    m = int(sys.stdin.readline()) #동전으로 만들어야하는 금액

    dp = [0] * (m+1)
    dp[0] = 1 #0을 만들 수 있는 가짓수는 항상 0이기 때문

    for coin in coins:
        for j in range(m+1):
            if j >= coin:
                dp[j] += dp[j-coin]
    print(dp[m])