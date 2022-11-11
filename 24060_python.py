import sys

def merge(arr,p,q,r):
    global cnt, result
    i = p
    j = q+1
    tmp = []

    while i<=q and j<=r:
        if arr[i] <= arr[j]:
            tmp.append(arr[i])
            i+=1
        else:
            tmp.append(arr[j])
            j+=1

    while i<=q:
        tmp.append(arr[i])
        i+=1

    while j <= r:
        tmp.append(arr[j])
        j+=1

    i = p
    t = 0

    while i <= r:
        arr[i] = tmp[t]
        cnt += 1
        if cnt == k:
            result = arr[i]
            break
        i += 1
        t += 1

def merge_sort(arr,p,r):
    if p < r:
        q = (p+r)//2
        merge_sort(arr,p,q)
        merge_sort(arr,q+1,r)
        merge(arr,p,q,r)



#n = 배열 a의 크기, k = 저장횟수
n,k = map(int,sys.stdin.readline().split()) #k번 째 저장되는 수 출력
arr = list(map(int,sys.stdin.readline().split()))
cnt = 0 #저장횟수, k보다 cnt가 크면 -1 출력
result = -1
merge_sort(arr,0,len(arr)-1)
print(result)