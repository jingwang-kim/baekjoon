import sys


t = int(sys.stdin.readline())
for _ in range(t):
    h,w,n = map(int,sys.stdin.readline().split())  #ex) 6 12 10
    num = n//h + 1  #방 번호 2
    floor = n % h   #객실 층 4
    if n%h == 0:
        num = n // h
        floor = h
    print(floor * 100 + num)