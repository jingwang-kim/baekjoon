import sys

n = int(sys.stdin.readline())
flag = 0
stack = []
answer = []

for i in range(n):
    k = int(sys.stdin.readline())
    if k >= flag:
        for j in range(flag+1,k+1):
            stack.append(j)
            answer.append('+')
    
    if stack[-1] == k:
        stack.pop()
        answer.append('-')
    flag = max(flag,k)

        
if len(stack) != 0:
    print('NO')
else:
    for i in range(len(answer)):
        print(answer[i])