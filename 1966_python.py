import sys
from collections import deque

t = int(sys.stdin.readline())
for _ in range(t):
    n,m = map(int,sys.stdin.readline().split())
    queue = deque(list(map(int,sys.stdin.readline().split())))
    result = 0

    while queue:
        flag = max(queue)
        target = queue.popleft()
        m-=1 

        if target == flag:
            result += 1
            if m<0:
                break
        else:
            queue.append(target)
            if m < 0:
                m = len(queue) - 1

    print(result)