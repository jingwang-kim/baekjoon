import sys

n = int(sys.stdin.readline())
list_t = [[0]*2 for _ in range(n)]

for i in range(n):
    s,e = map(int,input().split())
    list_t[i][0] = s
    list_t[i][1] = e

list_t.sort(key = lambda x : (x[1], x[0]))
flag = list_t[0][1]
cnt = 1

for i in range(1,n):
    if list_t[i][0] >= flag:
        cnt += 1
        flag = list_t[i][1]
print(cnt)