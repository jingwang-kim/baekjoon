import sys

def fibo_recur(n):
    if n == 1 or n == 2:
        return 1
    else:
        return (fibo_recur(n-1) + fibo_recur(n-2))

def fibo_dp(dp,n):
    dp[1] = dp[2] = 1
    cnt = 0
    for i in range(3,n+1):
        dp[i] = dp[i-1] + dp[i-2]
        cnt += 1
    return cnt


n = int(sys.stdin.readline())
dp = [0]*(n+1)
print(fibo_recur(n), fibo_dp(dp,n))