import sys

str = list(sys.stdin.readline())
m = int(sys.stdin.readline())
str.pop()
str.append(1)

for i in range(m):
    command = list(sys.stdin.readline())
    command.pop()
    cur = str.index(1)

    if command[0] == 'L':
        if str[0] == 1:
            continue
        str[cur], str[cur - 1] = str[cur -1], str[cur]
    
    elif command[0] == 'D':
        if str[-1] == 1:
            continue
        str[cur], str[cur +1] = str[cur +1], str[cur]
    
    elif command[0] == 'B':
        if str[0] == 1:
            continue
        del str[cur - 1]

    elif command[0] == 'P':
        str.insert(cur ,command[-1])

str.remove(1)
print("".join(str))