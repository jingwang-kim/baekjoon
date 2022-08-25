import sys
import math

#mCn
t = int(sys.stdin.readline())
for _ in range(t):
    n,m = map(int, sys.stdin.readline().split())
    result = math.factorial(m) // (math.factorial(n) * math.factorial(m-n))
    print(result)