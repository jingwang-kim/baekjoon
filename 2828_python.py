import sys

#n = 스크린, m = 바구니 칸 개수, j = 사과개수
n,m = map(int,sys.stdin.readline().split())
j = int(sys.stdin.readline())
apple = 0

left = 1
right = m
result = 0

for _ in range(j):
    apple = int(sys.stdin.readline())

    #사과가 바구니 안에 들어왔을 경우
    if apple >= left and apple <= right:
        continue

    #사과가 바구니보다 왼쪽에 있을 경우
    elif apple < left:
        result += left - apple  #result에 바구니와 사과의 거리만큼 더해줌
        left =apple             #사과가 있는 왼쪽으로 이동
        right = apple + (m-1)   #오른쪽은 사과위치 + 바구니의 칸 개수

    #사과가 바구니보다 오른쪽에 있을 경우
    elif apple > right:
        result += apple - right #result에 바구니와 사과의 거리만큼 더해줌
        left = apple - (m-1)    #왼쪽은 사과위치 + 바구니의 칸 개수
        right = apple           #사과가 있는 오른쪽으로 이동

print(result)