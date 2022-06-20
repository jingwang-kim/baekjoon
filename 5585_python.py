import sys

n = int(sys.stdin.readline())
change = [500,100,50,10,5,1]
n = 1000 - n
answer = 0

for i in change:
    answer += n // i
    n = n % i
print(answer)