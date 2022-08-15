import sys

t = int(sys.stdin.readline())
for _ in range(t):
    str = list(sys.stdin.readline())
    result = 0
    cnt = 0
    for i in str:
        if i == 'O':
            cnt += 1
            result += cnt
        elif i == 'X':
            cnt = 0
    print(result)