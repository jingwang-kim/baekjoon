import sys
from collections import deque

queue = deque([])
n = int(sys.stdin.readline())
for i in range(1,n+1):
    queue.append(i)
result = []

for _ in range(n-1):
    result.append(queue.popleft())
    queue.append(queue.popleft())
result.append(queue.popleft())

print(''.join(result))
for i in result:
    print(i, end=' ')