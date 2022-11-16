import sys

n = int(sys.stdin.readline())
result = []
for _ in range(n):
    x,y = map(int,sys.stdin.readline().split())
    result.append([x,y])

result.sort(key = lambda x: (x[1],x[0]))
for i in result:
    print(i[0], i[1])