import sys

a=int(sys.stdin.readline())
b=int(sys.stdin.readline())

b1=a*(b%10)
b2=a*((b//10)%10)
b3=a*(b//100)
result=a*b

print(b1,b2,b3,result,sep="\n")