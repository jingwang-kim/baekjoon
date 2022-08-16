import sys

t = int(sys.stdin.readline())

for _ in range(t):
    a,b = map(int,sys.stdin.readline().split())
    mini = maxi = 0

    #최소공배수
    a1,b1 = a,b    
    while True:
        if a1 == b1:
            mini = a1
            break
        elif a1 > b1:
            b1 += b
        elif a1 < b1:
            a1 += a
    
    #최대공약수
    for i in range(1,a+1):
        if a % i == 0 and b % i == 0:
            maxi = max(maxi, i)
    
    print(mini, maxi)