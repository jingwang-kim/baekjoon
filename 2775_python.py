import sys

t = int(sys.stdin.readline())

for _ in range(t):
    k = int(sys.stdin.readline()) #층
    n = int(sys.stdin.readline()) #호
    floor = [x for x in range(1,n+1)]

    for i in range(k):
        for j in range(1,n):
            floor[j] += floor[j-1]
    print(floor[-1])