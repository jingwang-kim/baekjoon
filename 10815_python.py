import sys

n = int(sys.stdin.readline())
card = sorted(list(map(int,sys.stdin.readline().split())))

m = int(sys.stdin.readline())
target = list(map(int,sys.stdin.readline().split()))


for i in target:
    flag = False
    start = 0
    end = n-1

    while start <= end:
        mid = (start+end)//2
        if card[mid] == i:
            flag = True
            break

        elif card[mid] > i:
            end = mid-1

        else:
            start = mid+1

    if flag:
        print(1, end=' ')
    else:
        print(0, end=' ')
