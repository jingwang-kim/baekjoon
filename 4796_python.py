import sys

i = 1
while True:
    #연속하는 p일 중, l일 동안만 캠핑장 이용 가능. v = 휴가일수 
    l,p,v = map(int,sys.stdin.readline().split())
    result = 0
    if l == 0 and p == 0 and v == 0:
        break

    while v >0:
        if v >= l:
            v -= p
            result += l

        else:
            result += v
            v -= p
    print(f'Case {i}: {result}')
    i+=1