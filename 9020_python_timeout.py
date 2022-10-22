import sys
import math

t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline()) #짝수
    result = []

    #에라스토테네스의 체
    for i in range(1,n):
        if i == 1:
            continue
        for j in range(2,int(math.sqrt(i)+1)):
            if i%j == 0:
                break

        else:
            if i not in result:
                result.append(i)


    answer=[]
    minu=[]
    for k in result:
        for h in result:
            if k+h == n:
                answer.append(k)
                answer.append(h)
                minu.append(abs(k-h))
    idx = minu.index(min(minu))
    for a in answer[idx*2:idx*2+2]:
        print(a, end=' ')
    print('')
    