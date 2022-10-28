import sys

n = int(sys.stdin.readline())
a = list(map(int,sys.stdin.readline().split()))
a.sort()

m = int(sys.stdin.readline())
target = list(map(int,sys.stdin.readline().split()))

for i in target:
    flag = False
    start = 0
    end = len(a)-1
    
    while start <= end:
        mid = (start+end)//2

        if a[mid] == i:
            flag = True
            break
        elif a[mid] < i:
            start = mid+1
        else:
            end = mid-1

    if flag:
        print(1)
    else:
        print(0)