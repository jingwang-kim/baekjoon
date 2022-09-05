import sys
from collections import deque

n = int(sys.stdin.readline())
queue = deque([])
for i in range(1,n+1):
    queue.append(i)
level = 1
idx = 0

while len(queue) > 1:

    flag = (level**3) % len(queue)
    if flag == 1:
        queue.popleft()
    else:
        queue.rotate(-(flag-1))
        queue.popleft()

    level += 1
print(queue[0])