import sys
from math import factorial as fac

# n! // k!(n-k)!

n,k = map(int,sys.stdin.readline().split())
result = fac(n) // (fac(k) * fac(n-k))
print(result)