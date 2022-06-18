import sys

while(True):
    stack = []
    sum = 0
    str = list(sys.stdin.readline())
    if str[0] == '.':
        break

    for i in range(len(str)):
        if str[i] == '(' or str[i] == '[':
            stack.append(str[i])
            sum += 1

        elif str[i] == ']':
            if len(stack) == 0:
                sum -= 1
                break
            else:
                if stack[-1] == '[':
                    stack.pop()
                    sum-=1
                else:
                    sum -= 10000
                    break

        elif str[i] == ')':
            if len(stack) == 0:
                sum -= 1
                break
            else:
                if stack[-1] == '(':
                    stack.pop()
                    sum-=1
                else:
                    sum -= 10000
                    break

        elif str[i] == '.':
            break
    
    if sum == 0:
        print('yes')
    else:
        print('no')