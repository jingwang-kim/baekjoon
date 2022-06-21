import sys

n = int(sys.stdin.readline())

for _ in range(n):
    str = list(sys.stdin.readline().rstrip())
    stack1 = [] 
    stack2 = [] 

    for i in range(len(str)):
        if str[i] == '<':
            if stack1:
                stack2.append(stack1.pop())
        elif str[i] == '>':
            if stack2:
                stack1.append(stack2.pop())
        elif str[i] == '-':
            if stack1:
                stack1.pop()
        else:
            stack1.append(str[i])


    stack1.extend(reversed(stack2))
    print("".join(stack1))