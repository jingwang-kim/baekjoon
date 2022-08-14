import sys

m = int(sys.stdin.readline())
n = int(sys.stdin.readline())
psn = []

for i in range(1,1001):
    sq = i * i

    if m <= sq <= n:
        psn.append(sq)
    
if len(psn) == 0:
    print(-1)

else:
    print(sum(psn))
    print(min(psn))