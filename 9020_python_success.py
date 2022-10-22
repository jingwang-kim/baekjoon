import sys
import math

def isPrime(n):
    if n == 1:
        return False
    for i in range(2,int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True

t = int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline())
    a, b = n//2, n//2

    while a > 0:
        if isPrime(a) and isPrime(b):
            print(a,b)
            break
        else:
            a-=1
            b+=1