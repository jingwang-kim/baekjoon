import sys

n,k = map(int,sys.stdin.readline().split())

score = sorted(list(map(int,sys.stdin.readline().split())))
print(score[-k])
