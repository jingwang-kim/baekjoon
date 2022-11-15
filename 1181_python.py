import sys

n = int(sys.stdin.readline())
result = []

for _ in range(n):
    result.append(sys.stdin.readline().rstrip())

result = list(set(result))
result.sort()
result.sort(key=lambda x:len(x))

for i in result:
    print(i)
