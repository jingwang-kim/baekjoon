import sys

n = int(sys.stdin.readline())
a = list(map(int,sys.stdin.readline().split()))
op = list(map(int,sys.stdin.readline().split())) # +, -, *, //

maxi = -sys.maxsize
mini = sys.maxsize

def back(depth, total, plus, minus, multiply, divide):
    global maxi, mini
    if depth == n:
        maxi = max(total, maxi)
        mini = min(total, mini)
        return
    
    if plus:
        back(depth+1, total + a[depth], plus-1, minus, multiply, divide)
    if minus:
        back(depth+1, total - a[depth], plus, minus-1, multiply, divide)
    if multiply:
        back(depth+1, total * a[depth], plus, minus, multiply-1, divide)
    if divide:
        back(depth+1, int(total / a[depth]), plus, minus, multiply, divide-1)


back(1,a[0],op[0],op[1],op[2],op[3])
print(maxi)
print(mini)