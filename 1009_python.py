import sys

t = int(sys.stdin.readline())

for _ in range(t):
    a,b = map(int,sys.stdin.readline().split())
    a %= 10

    if a == 0:
        print(10)
    elif a == 1 or a == 5 or a == 6:
        print(a)
    elif a == 4 or a == 9:
        b %= 2
        if b == 0:
            print(a*a%10)
        else:
            print(a)
    else:
        b %= 4
        if b == 0:
            print(a**4%10)
        else:
            print(a**b%10)