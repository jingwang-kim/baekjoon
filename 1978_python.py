import sys

n = int(sys.stdin.readline())
prime = list(map(int,sys.stdin.readline().split()))

def isprime(a):
    if a<2:
        return False
    for i in range(2,a):
        if a%i == 0:
            return False
    
    return True

result = 0
for i in prime:
    if(isprime(i)):
        result += 1

print(result)