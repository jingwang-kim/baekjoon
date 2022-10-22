import sys
import math

#시간 초과를 잡기 위해 미리 소수들을 저장해놓은 배열 생성
arr = [True for _ in range(2*123456+1)]
arr[0],arr[1] = False,False #True = 소수

#에라스토테네스의 체
for i in range(2,int(math.sqrt(2*123456)+1)):
    if arr:
        j=2
        while i*j <= 2*123456:
            arr[i*j] = False
            j+=1


while True:
    n = int(sys.stdin.readline())
    if n == 0:
        break

    result = 0
    for i in range(n+1,(n*2)+1):
        if arr[i]:
            result += 1

    print(result)