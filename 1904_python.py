import sys

def tile(n):
    dp = [0]*(n+1)
    dp[0] = dp[1] = 1
    for i in range(2,n+1):
        dp[i] = dp[i-1] + dp[i-2]
    print(dp)
    return dp[-1]


if __name__ == '__main__':
    n = int(sys.stdin.readline())
    print(tile(n) % 15746)
