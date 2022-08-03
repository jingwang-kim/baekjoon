import sys

str = sys.stdin.readline().split('-')
list_t = []
for i in str:
    cnt = 0
    tmp = i.split('+')
    for j in tmp:
        cnt += int(j)
    list_t.append(cnt)

result = list_t[0]
for i in range(1,len(list_t)):
    result -= list_t[i]
print(result)