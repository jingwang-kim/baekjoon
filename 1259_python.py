import sys
from collections import deque

while True:
    pail = list(map(int,sys.stdin.readline().rstrip()))

    if pail[0] == 0:
        break
    flag = True #False일 때 no, True일 때 yes
    queue = deque(pail)
    
    for i in range(len(pail)//2):
        if len(queue) == 1:
            break

        if queue.popleft() != queue.pop():
            flag = False
            break


    if flag:
        print('yes')
    else:
        print('no')
