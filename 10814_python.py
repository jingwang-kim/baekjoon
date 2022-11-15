import sys

n = int(sys.stdin.readline())
result = []

for _ in range(n):
    age,name = map(str,sys.stdin.readline().rstrip().split())
    age = int(age)
    result.append([age,name])
result.sort(key=lambda x: x[0])

for i in result:
    print(i[0], i[1])