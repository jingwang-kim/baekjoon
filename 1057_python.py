import sys

n, j_num, l_num = map(int,sys.stdin.readline().split())
result = 0

while j_num != l_num:
    j_num -= j_num // 2
    l_num -= l_num // 2
    result += 1
print(result)