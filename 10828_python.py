import sys

n = int(sys.stdin.readline())
list_s = []

for i in range(n):
    com = sys.stdin.readline().split()
    if com[0] == 'push':
        list_s.append(com[1])
    elif com[0] == 'pop':
        if len(list_s) == 0:
            print(-1)
        else:
            print(list_s.pop())
    elif com[0] == 'size':
        print(len(list_s))
    elif com[0] == 'empty':
        if len(list_s) == 0:
            print(1)
        else:
            print(0)
    elif com[0] == 'top':
        if len(list_s) == 0:
            print(-1)
        else:
            print(list_s[-1])



