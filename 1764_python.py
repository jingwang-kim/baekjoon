import sys

n,m = map(int,sys.stdin.readline().split())
listen = set()
see = set()

for _ in range(n):
    listen.add(sys.stdin.readline().rstrip())

for _ in range(m):
    see.add(sys.stdin.readline().rstrip())

result = sorted(list(listen & see))

result.sort()
print(len(result))
for j in result:
    print(j)