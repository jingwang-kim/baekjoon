import sys

n = int(sys.stdin.readline())
list_t = []
for i in range(n):
    list_t.append(int(sys.stdin.readline()))
list_t.sort(reverse = True)

answer = []
for i in range(n):
    answer.append(list_t[i] * (i+1))
print(max(answer))