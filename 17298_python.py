import sys

n = int(sys.stdin.readline())
data = list(map(int, sys.stdin.readline().split()))
answer = []
stack = []

for i in range(n):
    while stack and stack[-1] < data[i]:
        answer.append(data[i])
        stack.pop()
    stack.append(data[i])
answer.append(-1)
print(answer)