import sys

#작은 동전부터 해당 동전을 이용하여 m원을 만들 수 있는 경우의 수를 더한 뒤,
#다음 동전으로 넘어가서 이전 경우의 수에 해당 동전으로 만들 수 있는 경우의 수를 순차적으로 더해가며 답을 구함


t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    price = list(map(int,sys.stdin.readline().split()))
    m = int(sys.stdin.readline())

    dp = [0] * (m+1)
    dp[0] = 1
    
    for coin in price:
        for i in range(m+1):
            if i >= coin:
                dp[i] += dp[i-coin]
    
    print(dp[m])