import sys

n = int(sys.stdin.readline())
flag = n
tmp = 0
result = 0

while True:
    tmp = n // 10 + n % 10
    n = 10 * (n % 10) + tmp % 10
    result += 1
    if n == flag:
        break
print(result)