import sys

n = int(sys.stdin.readline())
body = []

for _ in range(n):
    weight, height = map(int,sys.stdin.readline().split())
    body.append((weight,height))


for i in body:
    cnt = 1
    for j in body:
        if i[0] < j[0] and i[1] < j[1]:
            cnt += 1
    print(cnt,end=' ')