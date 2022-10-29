import sys

n = int(sys.stdin.readline())
card = sorted(list(map(int,sys.stdin.readline().split())))

m = int(sys.stdin.readline())
target = list(map(int,sys.stdin.readline().split()))

#dict에 개수를 저장해놓고 key가 존재하면 개수를 반환하고 그 외에는 0을 반환하는 방법
cnt={}
for i in card:
    if i in cnt:
        cnt[i]+=1
    else:
        cnt[i]=1

for i in target:
    if i in cnt:
        print(cnt[i],end=' ')
    else:
        print(0,end=' ')