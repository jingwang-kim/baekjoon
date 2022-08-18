import sys

t = int(sys.stdin.readline())
for i in range(t):
    r,s = sys.stdin.readline().split()
    s = list(s)
    for j in s:
        print(j * int(r),end='')
    print()