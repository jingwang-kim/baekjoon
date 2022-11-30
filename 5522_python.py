import sys

result = 0
for _ in range(5):
    data = int(sys.stdin.readline())
    result += data
print(result)