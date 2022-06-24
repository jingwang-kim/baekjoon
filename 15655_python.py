import sys

n,m = map(int,sys.stdin.readline().split())
answer = []
list_n = list(map(int,sys.stdin.readline().split()))
list_n.sort()

def back(start):
    if len(answer) == m:
        print(' '.join(map(str,answer)))
        return
    for i in range(start,len(list_n)):
        if list_n[i] not in answer:
            answer.append(list_n[i])
            back(i+1)
            answer.pop()
back(0)