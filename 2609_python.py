import sys

def GCD(n,m):
    for i in range(min(n,m), 0, -1):
        if n % i == 0 and m % i == 0:
            return i

def LCM(n,m):
    for i in range(max(n,m), (n*m)+1):
        if i % n == 0 and i % m == 0:
            return i

        
n,m = map(int,sys.stdin.readline().split())
print(GCD(n,m))
print(LCM(n,m))