import sys

n = int(sys.stdin.readline())
p = list(map(int, sys.stdin.readline().split()))
p.sort()
result = 0
sum = 0

for i in p:
    sum += i
    result += sum
print(result)