import sys

n,m = map(int,sys.stdin.readline().split())
answer = []
list_n = list(map(int,sys.stdin.readline().split()))
list_n.sort()

def back():
    if len(answer) == m:
        print(' '.join(map(str,answer)))
        return
    for i in list_n:
        if i not in answer:
            answer.append(i)
            back()
            answer.pop()
back()