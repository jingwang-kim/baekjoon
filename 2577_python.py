import sys

target = 1
result = [0] * 10
for _ in range(3):
    num = int(sys.stdin.readline())
    target *= num
target = list(map(int,str(target)))

for i in target:
    result[i] += 1

print(*result, sep='\n')