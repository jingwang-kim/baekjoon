import sys

n = int(sys.stdin.readline())
common = list(map(int,sys.stdin.readline().split()))
common.sort()
if n == 1:
    print(common[0] ** 2)
else:
    print(common[0] * common[-1])