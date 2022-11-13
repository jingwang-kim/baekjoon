import sys

n = int(sys.stdin.readline())
result = []

for i in range(n):
    a,b = map(int,sys.stdin.readline().split())
    result.append([a,b])
result.sort(key=lambda x: (x[0],x[1]))

for i in result:
    print(i[0], i[1])