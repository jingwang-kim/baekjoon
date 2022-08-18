import sys

n = int(sys.stdin.readline())
result = 0
flag = 0

for _ in range(n):
    s = list(sys.stdin.readline().strip())
    if len(s) == 1:
        result += 1
        continue

    for i in range(len(s)-1):
        if s[i-len(s)+1] != s[i] and s[i] in s[i-len(s)+1:len(s)]:
            flag = 0
            break
        else:
            flag = 1

    if flag == 1:
        result += 1

print(result)