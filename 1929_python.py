import sys

m,n = map(int,sys.stdin.readline().split())

for i in range(m,n+1):
    if i==1:
        continue
    for j in range(2,int(i**0.5)+1): #제곱근까지 구하는게 포인트
        if i%j == 0:
            break
    else:
        print(i)

#<에라스토테네스의 체>
#1은 소수가 아니므로 제외
#자기 자신을 제외한 2의 배수를 다 제거
#남아있는 숫자 중 자기자신을 제외한 3의 배수 다 제거
#이런 식으로 전부다 제거하는 과정