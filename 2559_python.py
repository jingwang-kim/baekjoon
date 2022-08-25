import sys

n,k = map(int,sys.stdin.readline().split())
arr_n = list(map(int,sys.stdin.readline().split()))
arr_n.insert(0,0)

for i in range(1,n+1):
    arr_n[i] = arr_n[i-1] + arr_n[i]

result = -987654321
for i in range(1,n-k+2):
    result = max(arr_n[i+k-1] - arr_n[i-1], result)

print(result)