import sys

n = int(sys.stdin.readline())
for i in range(n):
    list_v = list(sys.stdin.readline())
    stack = []
    sum = 0
    for i in range(len(list_v)):
        if list_v[i] == '(':
            stack.append(list_v[i])
            sum += 1
        elif list_v[i] == ')':
            if len(stack) == 0:
                sum -= 1
                break
            else:                
                stack.pop()
                sum -= 1
    if sum == 0:
        print('YES')
    else:
        print('NO')