import sys
from collections import deque

n,k = map(int,sys.stdin.readline().split())
queue = deque([])
for i in range(1,n+1):
    queue.append(i)
result = []

while queue:
    for i in range(k-1):
        queue.append(queue.popleft())
    result.append(queue.popleft())

print('<',end='')
for i in range(len(result)-1):
    print("%d, " %result[i],end='')
print(result[-1],end='')
print('>')