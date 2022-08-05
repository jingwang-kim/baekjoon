import sys

arr = []
result = 0
for _ in range(10):
    num = int(sys.stdin.readline()) % 42
    if num in arr:
        continue
    else:
        arr.append(num)
        result += 1

print(result)