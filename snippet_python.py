import sys
from collections import deque

#분할 정복
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

#분할정복의 거듭제곱 연산(나머지 분배법칙)
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