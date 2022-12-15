import sys

n = int(sys.stdin.readline())
a = list(map(int,sys.stdin.readline().split()))
dpi = [0 for _ in range(n)]
dpr = [0 for _ in range(n)]
dpb = [0 for _ in range(n)]

#바이토닉 수열 : 1 2 3 2 1 처럼 숫자가 산을 이루는 수열
# 5 4 3 2, 1 2 3 4 도 바이토닉 수열임

#10
#1 5 2 1 4 3 4 5 2 1

#증가
for i in range(n):
    for j in range(i):
        if a[i] > a[j] and dpi[i] < dpi[j]:
            dpi[i] = dpi[j]
    dpi[i] += 1

#감소
for i in range(n-1,-1,-1):
    for j in range(n-1,i,-1):
        if a[i] > a[j] and dpr[i] < dpr[j]:
            dpr[i] = dpr[j]
    dpr[i] += 1

for i in range(n):
    dpb[i] = dpr[i] + dpi[i] - 1 

print(max(dpb))