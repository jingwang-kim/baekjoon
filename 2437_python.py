import sys

n = int(sys.stdin.readline())
weight = list(map(int,sys.stdin.readline().split()))

weight.sort()
result = 1

for i in weight:
    if result < i:
        break
    result += i

print(result)