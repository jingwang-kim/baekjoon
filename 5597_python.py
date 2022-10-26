import sys

arr = []
for _ in range(28):
    arr.append(int(sys.stdin.readline()))

for i in range(1,30):
    if i not in arr:
        print(i)