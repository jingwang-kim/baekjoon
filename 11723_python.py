import sys

m = int(sys.stdin.readline())
s = set()
for _ in range(m):
    tmp = sys.stdin.readline().strip().split()

    if len(tmp) == 1:
        if tmp[0] == 'all':
            s = set([i for i in range(1,21)])
        else:
            s = set()
    
    else:
        func,x = tmp[0], tmp[1]
        x = int(x)

        if func == 'add':
            s.add(x)
        elif func == 'remove':
            s.discard(x)
        elif func == 'check':
            print(1 if x in s else 0)
        elif func == 'toggle':
            if x in s:
                s.discard(x)
            else:
                s.add(x)