import sys

n = list(sys.stdin.readline().rstrip())
n.sort(reverse=True)
answer = int("".join(n))
if answer % 30 == 0:
    print(answer)
else:
    print(-1)