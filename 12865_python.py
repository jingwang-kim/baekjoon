import sys

n,k = map(int,sys.stdin.readline().split())

thing = [[0,0]]
for _ in range(n):
    thing.append(list(map(int,sys.stdin.readline().split())))
dp = [[0 for _ in range(k+1)] for _ in range(n+1)]

# i : 현재 담을 물건의 index
# j : 현재 가방 허용 용량
# weight : 현재 담을 물건의 무게
# value : 물건의 가치
for i in range(1,n+1):
    for j in range(1,k+1):
        weight = thing[i][0]
        value = thing[i][1]

        #현재 배낭의 허용 무게보다 넣을 물건의 무게가 더 크다면 넣지 않는다.
        if j < weight:
            dp[i][j] = dp[i-1][j]
        
        #현재 넣을 물건의 무게만큼 배낭에서 빼고 현재 물건을 넣는 경우
        #현재 물건을 넣지 않고 이전 배낭 그대로 가져오는 경우
        #위의 경우 2개 중 더 나은 가치를 선택하여 넣는다.
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-weight]+value)
print(dp[n][k])