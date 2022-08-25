import sys

n,m = map(int,sys.stdin.readline().split())
arr_n = list(map(int,sys.stdin.readline().split()))
arr_n.insert(0,0)
for i in range(1,n+1):
    arr_n[i] = arr_n[i-1] + arr_n[i]

result = 0
for i in range(1,n+1):
    for j in range(i,n+1):
        if (arr_n[j] - arr_n[j-i]) % m == 0:
            result += 1

print(result)
