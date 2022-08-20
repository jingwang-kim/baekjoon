import sys
#P(N) = P(N-1) + P(N-5)
dp = [0] * 101
dp[1] = 1
dp[2] = 1
dp[3] = 1
dp[4] = 2
dp[5] = 2

def triangle(n):
    for i in range(6, 101):
        dp[i] = dp[i-1] + dp[i-5]
    
    return dp[n]


if __name__ == '__main__':
    t = int(sys.stdin.readline())
    
    for _ in range(t):
        n = int(sys.stdin.readline())
        print(triangle(n))