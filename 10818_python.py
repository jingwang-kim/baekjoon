import sys

n=int(sys.stdin.readline())
a=list(map(int,sys.stdin.readline().split()))
print("{} {}".format(min(a), max(a)))