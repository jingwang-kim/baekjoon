import sys

def binary_search(card,target,start,end):
    if start > end:
        return 0
    mid = (start+end)//2

    #target을 찾으면 cnt에서 target key에 맞는 value 출력
    if card[mid] == target:
        return cnt.get(target) #get은 key를 이용하여 value를 얻는 방법
    
    elif card[mid] < target:
        return binary_search(card,target,mid+1,end)
    
    else:
        return binary_search(card,target,start,mid-1)

n = int(sys.stdin.readline())
card = sorted(list(map(int,sys.stdin.readline().split())))

m = int(sys.stdin.readline())
target = list(map(int,sys.stdin.readline().split()))

#이 방법을 생각하지 못함
#cnt 안에 이미 들어있는 key는 +=1을 해주고, 새로운 key가 삽입되면 1로 초기화해줌
cnt = {}
for i in card:
    if i in cnt:
        cnt[i] += 1
    else:
        cnt[i] = 1

for i in target:
    print(binary_search(card,i,0,len(card)-1),end=' ')