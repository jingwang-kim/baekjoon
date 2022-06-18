import sys

str = list(sys.stdin.readline())
print(str)
sum = 0
answer =0
for i in range(len(str)):
    if str[i] == '(':
        sum += 1

    elif str[i] == ')':
        if str[i-1] == '(':
            sum -= 1
            answer += sum
        else:
            sum -= 1
            answer += 1
print(answer)