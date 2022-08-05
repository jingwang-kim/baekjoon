import sys

def facto(num,res):
    if num == 0:
        return res
    else:
        res*=num
        return facto(num-1,res)

n=int(sys.stdin.readline())
res = 1
print(facto(n,res))