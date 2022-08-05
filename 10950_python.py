import sys

test=int(sys.stdin.readline())

for i in range(0,test):
    a,b=map(int,sys.stdin.readline().split())
    print(a+b)