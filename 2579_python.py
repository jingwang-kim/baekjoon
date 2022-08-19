import sys

'''
<dp>
처음 10 #초기값
첫 번째 경우 10+20 or 20 (1 2 or 2) #1 갔다가 2 밟거나 바로 2 밟거나
두 번째 경우 10+15 or 20+15(1 3 or 2 3) #1갔다가 3 밟거나 2갔다가 3밟거나

<조건>
1. 마지막 계단 - 1 밟았을 경우 : 현재칸 + 그 전칸 + 3번째 전 칸
2. 마지막 계단 - 2 밟았을 경우 : 현재칸 + 2번째 전 칸
'''

def max_stair(stair,n):
    dp = []
    dp.append(stair[0])
    dp.append(max(stair[1], stair[0] + stair[1]))
    dp.append(max(stair[0] + stair[2], stair[1] + stair[2]))
    for i in range(3, n):
        dp.append(max(dp[i-2] + stair[i],dp[i-3] + stair[i] + stair[i-1]))
    return dp.pop()


if __name__ == '__main__':
    n = int(sys.stdin.readline())
    stair = []
    for _ in range(n):
        stair.append(int(sys.stdin.readline()))
    if n == 1 or n == 2:
        print(sum(stair))
    else:
        print(max_stair(stair,n))