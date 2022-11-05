import sys
import heapq

n = int(sys.stdin.readline())
hq = []

for i in range(n):
    x = int(sys.stdin.readline())
    if x == 0:
        if hq:
            print(heapq.heappop(hq)[1])
        else:
            print(0)
    else:
        #heap을 tuple로 구성 시 맨 앞 숫자만으로 정렬하므로 abs내장함수 사용
        #tuple로 저장하는 법 숙지해야함
        heapq.heappush(hq,(abs(x),x))