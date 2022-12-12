import sys

n = int(sys.stdin.readline())
t=[] #소요시간
p=[] #얻는비용
dp = []

for _ in range(n):
    t_tmp, p_tmp = map(int,sys.stdin.readline().split())
    t.append(t_tmp)
    p.append(p_tmp)
    dp.append(p_tmp)

dp.append(0)
for i in range(n-1,-1,-1):
    if t[i] + i > n:  #지금 일을 함으로써 n을 넘어가게 되면
        dp[i] = dp[i+1] #일을 안함(그 전 값이 최댓값)
    else: #n을 넘지 않으면 일을 함
        dp[i] = max(dp[i+1], p[i] + dp[i+t[i]]) #그 전 값과 현재비용에 전에 일한 날짜의 비용을 더한 값 중 더 큰 값 선택
print(dp[0])
