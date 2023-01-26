import sys
from collections import deque

#<분할 정복>
n = int(sys.stdin.readline())
graph = [list(map(int,sys.stdin.readline().strip())) for _ in range(n)]

def solution(x,y,n):
    check = graph[x][y]
    for i in range(x,x+n):
        for j in range(y,y+n):
            if check != graph[i][j]:
                print('(', end='')
                solution(x,y,n//2)
                solution(x,y+n//2,n//2)
                solution(x+n//2,y,n//2)
                solution(x+n//2,y+n//2,n//2)
                print(')', end='')
                return
            
    if check == 0:
        print(0, end='')
    else:
        print(1, end='')

solution(0,0,n)



#<분할정복의 거듭제곱 연산(나머지 분배법칙)>
#지수 법칙 : a^m+n = a^m * a^n
#나머지 분배 법칙 : (a*b) % c = ((a%c) * (b%c)) % c

a,b,c = map(int,sys.stdin.readline().split()) # a ^ b % c
# ex) a = 10, b = 11, c = 12
# ((10^5)%12 * (10^5) % 12 * 10) % 12
# ((10^2)%12 x (10^2)%12 x 10) %12 x (10^2)%12 x (10^2)%12 x 10) %12 x 10) %12

def solve(a,b,c):
    if b == 1:
        return a%c
    if b % 2 == 0:
        return (solve(a,b//2,c)**2)%c
    else:
        return ((solve(a,b//2,c)**2)*a)%c

print(solve(a,b,c))



#<배낭문제(knapsack)>
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

