import sys

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