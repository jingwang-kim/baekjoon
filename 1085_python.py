import sys

x,y,w,h = map(int,sys.stdin.readline().split())
result = min(min(abs(x-w),abs(y-h)),min(abs(x-0),abs(y-0)))
print(result)