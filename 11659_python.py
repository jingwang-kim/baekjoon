import sys

n,m = map(int,sys.stdin.readline().split())
arr_n = list(map(int,sys.stdin.readline().split()))
for i in range(1,n):
    arr_n[i] = arr_n[i-1] + arr_n[i]
arr_n.insert(0,0)
for _ in range(m):
    m1,m2 = map(int,sys.stdin.readline().split())
    print(arr_n[m2] - arr_n[m1-1])