import sys

n = int(sys.stdin.readline())
arr = list(map(int,sys.stdin.readline().split()))
dp=[0]*n

for i in range(n):
    for j in range(i):
        #자기 자신보다 작은 숫자들 중 가장 큰 길이 구하고
        #그 길이에 +1
        if arr[i] > arr[j] and dp[i] < dp[j]:
            dp[i] = dp[j]
    dp[i] += 1

print(max(dp))