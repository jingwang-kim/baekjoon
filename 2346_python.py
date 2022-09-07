import sys
from collections import deque

n = int(sys.stdin.readline())
queue = deque([])
for i in range(1,n+1):
    queue.append(i)

balloon = deque(list(map(int,sys.stdin.readline().split())))

while queue:
    result = queue.popleft() #답
    tmp = balloon.popleft() #다음번째 풍선

    if tmp > 0:
        queue.rotate(-(tmp-1)) #양수면 오른쪽 음수면 왼쪽
        balloon.rotate(-(tmp-1))
    else:
        queue.rotate(-tmp) #양수면 오른쪽 음수면 왼쪽
        balloon.rotate(-tmp)
    print(result,end=' ')