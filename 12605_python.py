import sys

n = int(sys.stdin.readline())
for i in range(1,n+1):
    answer = list(sys.stdin.readline().rstrip().split())
    print('Case #%d: %s' %(i, ' '.join(answer[::-1])))