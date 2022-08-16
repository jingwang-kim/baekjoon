import sys

c = int(sys.stdin.readline())

for _ in range(c):
    ave = list(map(int,sys.stdin.readline().split()))
    flag = sum(ave[1:])/ ave[0]
    result = cnt = 0

    for i in ave[1:]:
        if i > flag:
            cnt += 1

    cnt*=100
    result = round(float(cnt) / float(ave[0]), 3)
    print(f'{result:.3f}%')
