import sys

n,s = map(int,sys.stdin.readline().split())
arr = list(map(int,sys.stdin.readline().split()))
result = 0

def back(idx, sum):
    global result

    if idx >=n :
        return
    
    sum+=arr[idx]

    if sum == s:
        result += 1
    
    back(idx+1, sum)
    back(idx+1, sum - arr[idx])

back(0,0)
print(result)