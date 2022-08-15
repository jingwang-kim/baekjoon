import sys

n = int(sys.stdin.readline())
flag = 0
title = 666

while True:
    if '666' in str(title):
        flag += 1

    if flag == n:
        print(title)
        break

    title += 1