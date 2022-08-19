import sys

n = int(sys.stdin.readline())
flag = 1
result = 1

while n > flag:
    flag += result * 6
    result += 1
print(result)