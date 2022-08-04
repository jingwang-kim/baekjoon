import sys

#n = 과일개수, l = 스네이크버드 초기 길이
n,l = map(int,sys.stdin.readline().split())
fruit = list(map(int, sys.stdin.readline().split()))
fruit.sort()

for i in fruit:
    if i > l:   #스네이크버드의 길이가 과일 높이보다 짧을 때
        break

    elif i <= l:#스네이크버드의 길이가 과일 높이보다 길거나 같을 때
        l += 1
print(l)