import sys

check = list(map(int,sys.stdin.readline().split()))
result = 0
for i in check:
    result += i**2

print(result%10)