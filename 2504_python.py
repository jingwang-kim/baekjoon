import sys

str = list(sys.stdin.readline().rstrip())
answer = 0
tmp = 1
stack = []

for i in range(len(str)):
    if str[i] == '(':
        stack.append(str[i])
        tmp *= 2

    elif str[i] == '[':
        stack.append(str[i])
        tmp *= 3

    elif str[i] == ')':
        if not stack or stack[-1] == '[':
            answer = 0
            break

        if str[i-1] == '(':
            answer+=tmp
        tmp //=2
        stack.pop()

    elif str[i] == ']':
        if not stack or stack[-1] == '(':
            answer = 0
            break

        if str[i-1] == '[':
            answer+=tmp
        tmp //=3
        stack.pop()

if stack:
    print(0)
else:
    print(answer)