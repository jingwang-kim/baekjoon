import sys

t = int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline())
    audit = []

    for _ in range(n):
        a,b = list(map(int,sys.stdin.readline().split()))
        audit.append([a,b])
    
    audit.sort()
    answer = 1
    best = audit[0][1]

    for i in range(n):
        if best > audit[i][1]:
            best = audit[i][1]
            answer += 1
    
    print(answer)