import sys

while True:
    n = int(sys.stdin.readline())
    if n == 0:
        break

    result=[]
    for i in range(n+1,(n*2)+1):

        if i == 1:
            continue

        for j in range(2,int(i**0.5)+1):
            if i%j == 0:
                break

        else:
            if i not in result:
                result.append(i)
    print(len(result))