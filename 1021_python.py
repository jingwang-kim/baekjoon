import sys
from collections import deque

n,m = map(int,sys.stdin.readline().split())
queue = deque([])
for i in range(1,n+1):
    queue.append(int(i))
index = list(map(int,sys.stdin.readline().split()))

result = 0

for i in index:
    while True:
        if queue[0] == i:
            queue.popleft()
            break
        else:
            if queue.index(i) < len(queue)/2:
                while queue[0] != i:
                    queue.append(queue.popleft())
                    result += 1
            else:
                while queue[0] != i:
                    queue.appendleft(queue.pop())
                    result += 1

print(result)