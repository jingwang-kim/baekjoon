import sys

n,m = map(int,sys.stdin.readline().split())
answer = []

def back(start):
    if len(answer) == m:
        print(' '.join(map(str,answer)))
        return
    
    for i in range(start,n+1):
        if i not in answer:
            answer.append(i)
            back(i+1)
            answer.pop()
back(1)