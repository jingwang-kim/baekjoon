import sys
from collections import deque

t = int(sys.stdin.readline())
for _ in range(t):
    p = list(sys.stdin.readline().rstrip())
    n = int(sys.stdin.readline())
    queue = deque(map(int,sys.stdin.readline().rstrip()[1:-1].replace(',','')))
    flag = 1

    for i in p:
        if i == "R":
            queue.reverse()
        
        elif i == "D":
            if queue:
                queue.popleft()
            else:
                flag = 0
                break
    
    if flag == 0:
        print("error")
    else:
        print(list(queue))