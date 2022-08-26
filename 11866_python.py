import sys
from collections import deque

n,k = map(int,sys.stdin.readline().split())
queue = deque([])
result = []

for i in range(1,n+1):
    queue.append(i)

while queue:
    for i in range(k-1):
        queue.append(queue.popleft()) #k-1 개만큼 뒤로 이동시키면 k번째 사람이 제일 앞에 옴
    result.append(queue.popleft())    #제일 앞에 있는걸 빼면 요세푸스 문제 풀이 완료

print('<',end='')
for i in range(len(result)-1):
    print("%d, "%result[i],end='')
print(result[-1],end='')
print('>')