import sys

n = int(sys.stdin.readline())
grade = list(map(int,sys.stdin.readline().split()))
maxi = max(grade)
result = 0

for i in range(n):
    grade[i] = grade[i] / maxi* 100

result = float(sum(grade)) / float(n)
print(result)