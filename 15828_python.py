import sys
from collections import deque

n = int(sys.stdin.readline())
queue = deque([])

while True:
    r = int(sys.stdin.readline())
    if r == -1:
        break
    if r == 0:
        if queue:
            queue.popleft()
        else:
            continue
    elif r != 0 and len(queue) < n:
        queue.append(r)
    
if queue:
    for i in queue:
        print(i,end=' ')
else:
    print('empty')