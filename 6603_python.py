import sys

answer = []


def back(start):
    if len(answer) == 6:
        print(' '.join(map(str,answer)))
        return
    for i in range(start, len(data)):
        if data[i] not in answer:
            answer.append(data[i])
            back(i)
            answer.pop()

while True:
    data = list(map(int, sys.stdin.readline().split()))
    if data[0] == 0:
        break
    del data[0]
    back(0)
    print()