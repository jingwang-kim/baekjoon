import sys

m = int(sys.stdin.readline())
n = int(sys.stdin.readline())

def isprime(a):
    if a<2:
        return False
    
    for i in range(2,a):
        if a % i == 0:
            return False
    
    return True



sum = 0
mini = n
flag = False
for i in range(m,n+1):
    if (isprime(i)):
        flag = True
        sum += i
        mini = min(mini,i)

if flag:
    print(sum)
    print(mini)
else:
    print(-1)