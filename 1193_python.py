import sys

x = int(sys.stdin.readline())
#홀수씩 늘어날 때 : 분자는 n -> 1, 분모는 1 -> n  ex) 3/1 -> 2/2 -> 1/3
#짝수씩 늘어날 때 : 분자는 1 -> n, 분모는 n -> 1  ex) 1/2 -> 2/1

flag = 1
while x > flag:
    x -= flag
    flag += 1
    print(x, flag)

if flag % 2 == 0:
    child = x
    mother = flag - x + 1
else:
    child = flag - x + 1
    mother = x
print(child,'/',mother,sep='')