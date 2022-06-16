import sys

n = int(sys.stdin.readline())
result = 0

while n >= 0:
    if n % 5 == 0:
        result += n//5
        n = n % 5
        break
    n -= 3
    result += 1

if n == 0:
    print(result)
else:
    print(-1)