import sys

n = int(sys.stdin.readline())
tmp = []
for _ in range(n):
    tmp.append(int(sys.stdin.readline()))

result = sorted(tmp)
for i in range(len(tmp)):
    print(result[i])