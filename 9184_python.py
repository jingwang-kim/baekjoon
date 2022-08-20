import sys
dp = [[[0] * 21 for _ in range(21)] for _ in range(21)]
def go_func(a,b,c):

    if a <=0 or b<=0 or c<=0:
        return 1

    if a>20 or b>20 or c>20:
        return go_func(20,20,20)

    if dp[a][b][c]:
        return dp[a][b][c]

    if a<b<c:
        dp[a][b][c] = go_func(a,b,c-1) + go_func(a,b-1,c-1) - go_func(a,b-1,c)
        return dp[a][b][c]

        
    dp[a][b][c] = go_func(a-1,b,c) + go_func(a-1,b-1,c) + go_func(a-1,b,c-1)- go_func(a-1,b-1,c-1)
    return dp[a][b][c]
    


if __name__ == '__main__':
    while True:
        a,b,c = map(int,sys.stdin.readline().split())
        if a == -1 and b == -1 and c == -1:
            break
        print(f'w({a}, {b}, {c}) = {go_func(a,b,c)}')