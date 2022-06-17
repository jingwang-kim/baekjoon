import sys

n = int(sys.stdin.readline())
list_a = list(map(int,sys.stdin.readline().split()))
list_b = list(map(int,sys.stdin.readline().split()))
result = 0

list_a.sort()
list_b.sort(reverse = True)
for i in range(n):
    result += list_a[i] * list_b[i]
print(result)