import sys

n = int(sys.stdin.readline())
flag = 0
cnt = 1

while True:
    flag += cnt
    if flag == n:
        print(cnt)
        break
    elif flag > n:
        cnt-=1
        print(cnt)
        break
    cnt += 1
    