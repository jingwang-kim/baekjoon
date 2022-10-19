import sys
from collections import deque

#R이 들어올 때마다 reverse 하면 시간초과
t = int(sys.stdin.readline())
for _ in range(t):
    p = list(sys.stdin.readline().rstrip())
    n = int(sys.stdin.readline())
    arr = input()[1:-1].split(',')
    queue = deque(arr)
    flag = 1
    rev = 0 #0이면 안뒤집힌거 1이면 뒤집힌거

    if n == 0:
        queue = []

    for i in p:
        if i == "R":
            if rev == 1:
                rev = 0
            else:
                rev = 1
        
        elif i == "D":
            if queue:
                if rev == 1:
                    queue.pop()
                else:
                    queue.popleft()
            else:
                flag = 0
                break

    if flag == 0:
        print("error")
    else:
        if rev == 1:
            queue.reverse()
            print("["+",".join(queue)+"]")
        else:
            print("["+",".join(queue)+"]")