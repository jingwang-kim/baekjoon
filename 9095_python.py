import sys

t = int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline())
    result = [0]*11
    result[0] = 1
    result[1] = 2
    result[2] = 4

    for i in range(3,11):
        result[i] = result[i-3] + result[i-2] + result[i-1]
        
    print(result[n-1])