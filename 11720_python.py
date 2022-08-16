import sys

n = int(sys.stdin.readline())
m = sys.stdin.readline().strip()

result = list(map(int,m))
print(sum(result))