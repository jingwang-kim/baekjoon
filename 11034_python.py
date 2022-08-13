import sys

while True:
    try:
        a,b,c = map(int,sys.stdin.readline().split())
        dist = max(abs(a-b), abs(b-c)) - 1
        print(dist)
    except:
        exit()