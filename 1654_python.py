import sys

k,n = map(int,sys.stdin.readline().split())
arr = []
for _ in range(k):
    arr.append(int(sys.stdin.readline()))

start = 1
end = max(arr)

while start<=end:

    mid = (start+end)//2
    line = 0

    #line에 i를 mid로 나누어서 몇 개의 랜선이 만들어지는지 파악
    for i in arr:
        line += i // mid

    #랜선이 n개보다 더 많이 만들어지면 자르려는 랜선의 개수를 줄이기 위해
    #start를 mid+1로 변경
    if line >= n:
        start = mid+1
    #그렇지 않다면 end를 mid-1로 변경
    else:
        end = mid -1

print(end)