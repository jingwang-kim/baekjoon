import sys

n,m = map(int,sys.stdin.readline().split())
height = list(map(int,sys.stdin.readline().split()))

start = 0
end = max(height)

while start <= end:
    mid = (start+end)//2
    tree = 0
    for i in height:
        if i > mid:
            tree += i-mid
        if tree >m:
            break
        
    if tree >= m:
        start = mid +1
        
    else:
        end = mid-1
print(end)