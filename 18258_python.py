import sys

n = int(sys.stdin.readline())
queue = []
for _ in range(n):
    str = list(sys.stdin.readline().split())

    if str[0] == 'push':
        queue.append(str[-1])

    elif str[0] == 'pop':
        if queue:
            print(queue.pop(0))
        else:
            print(-1)

    elif str[0] == 'size':
        print(len(queue))

    elif str[0] == 'empty':
        if len(queue) == 0:
            print(1)
        else:
            print(0)

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