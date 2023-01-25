import sys

n = sorted(list(map(int,sys.stdin.readline().strip())),reverse = True)

for i in n:
    print(i,end='')