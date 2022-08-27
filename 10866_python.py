import sys
from collections import deque

n = int(sys.stdin.readline())
queue = deque([])
for _ in range(n):
    str = list(sys.stdin.readline().split())

    if str[0] == 'push_front':
        queue.appendleft(str[-1])

    elif str[0] == 'push_back':
        queue.append(str[-1])

    elif str[0] == 'pop_front':
        if queue:
            print(queue.popleft())
        else:
            print(-1)

    elif str[0] == 'pop_back':
        if queue:
            print(queue.pop())
        else:
            print(-1)

    elif str[0] == 'size':
        print(len(queue))

    elif str[0] == 'empty':
        if queue:
            print(0)
        else:
            print(1)

    elif str[0] == 'front':
        if queue:
            print(queue[0])
        else:
            print(-1)

    elif str[0] == 'back':
        if queue:
            print(queue[-1])
        else:
            print(-1)