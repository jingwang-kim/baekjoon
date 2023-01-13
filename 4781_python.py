import sys

#칼로리의 합이 가장 크게 되는 지를 구하는 문제

while True:
    n,m = map(float, sys.stdin.readline().strip().split())
    n,m = int(n), int(m * 100 + 0.5) #float의 부동소수점 오류를 해결하기 위해 0.5를 더해줌

    if n == 0 and m == 0:
        break

    dp = [0] * (m+1)
    for _ in range(n):
        calories,price = map(float, sys.stdin.readline().strip().split())
        calories,price = int(calories), int(price * 100 + 0.5)

        for i in range(price, m+1):
            dp[i] = max(dp[i], dp[i-price] + calories)
    
    print(dp[m])