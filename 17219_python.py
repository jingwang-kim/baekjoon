import sys

n,m = map(int,sys.stdin.readline().split())

save = {}

for _ in range(n):
    a,b = map(str,sys.stdin.readline().rstrip().split())
    save[a] = b

for _ in range(m):
    find = sys.stdin.readline().rstrip()
    print(save[find])