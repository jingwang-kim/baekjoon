import sys

a,b = map(int,sys.stdin.readline().split())

a = list(map(str,str(a)))
b = list(map(str,str(b)))
print(a,b)

aa = ''.join(reversed(a))
bb = ''.join(reversed(b))
print(aa,bb)

print(max(int(aa),int(bb)))