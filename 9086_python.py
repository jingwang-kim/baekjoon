import sys

t = int(sys.stdin.readline())
for _ in range(t):
    str = list(sys.stdin.readline().rstrip())
    print(str[0],end = '')
    print(str[-1])