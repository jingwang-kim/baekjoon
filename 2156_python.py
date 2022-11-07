import sys

'''
포도주 잔을 선택하면 그 잔에 들어있는 포도주는 모두 마셔야 하고, 
마신 후에는 원래 위치에 다시 놓아야 한다.

연속으로 놓여 있는 3잔을 모두 마실 수는 없다.
'''


n = int(sys.stdin.readline())

wine = [0]
for _ in range(n):
    wine.append(int(sys.stdin.readline()))

dp = [0]*(n+1)
dp[1] = wine[1]


for i in range(2,n+1):
    dp[i] = max(dp[i-2] + wine[i], dp[i-1], dp[i-3]+wine[i-1]+wine[i])

print(dp[-1])